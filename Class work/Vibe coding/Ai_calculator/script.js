/* ==========================================================================
   AI Calculator - Simple JavaScript Implementation
   Clean, beginner-friendly, and fully functional. No eval() used.
   ========================================================================== */

// --- 1. State Variables ---
let currentInput = "0";             // Current number string being entered
let equationTokens = [];            // Stores numbers & operators, e.g. ["15", "+", "3"]
let isCalculationFinished = false;  // Flag set to true immediately after '=' is pressed
let history = [];                   // Stores history records: { equation, result, time }

// --- 2. DOM Elements Selection ---
const displayMain = document.getElementById("display-main");
const displayExpression = document.getElementById("display-expression");
const displayPreview = document.getElementById("display-preview");
const copyAlert = document.getElementById("copy-alert");
const copyBtn = document.getElementById("copy-btn");
const themeToggleBtn = document.getElementById("theme-toggle-btn");
const themeIcon = document.getElementById("theme-icon");
const historyToggleBtn = document.getElementById("history-toggle-btn");
const historyPanelContainer = document.getElementById("history-panel-container");
const historyList = document.getElementById("history-list");
const clearHistoryBtn = document.getElementById("clear-history-btn");
const historyBadge = document.getElementById("history-badge");

// All keypad buttons
const allButtons = document.querySelectorAll(".calc-btn");

// --- 3. Core Calculator Functions ---

/**
 * Updates the calculator screen display with current numbers and formatting
 */
function updateDisplay() {
  // Update main display text
  displayMain.textContent = currentInput;

  // Dynamically scale font size if the number is very long
  if (currentInput.length > 14) {
    displayMain.className = "display-main text-end font-small";
  } else if (currentInput.length > 9) {
    displayMain.className = "display-main text-end font-medium";
  } else {
    displayMain.className = "display-main text-end";
  }

  // Update the top expression line (e.g., "12 + 4 ×")
  if (equationTokens.length > 0) {
    displayExpression.textContent = equationTokens.join(" ");
  } else if (!isCalculationFinished) {
    displayExpression.textContent = "";
  }

  // Update instant live calculation preview
  updateLivePreview();
}

/**
 * Appends a digit (0-9) to currentInput
 */
function appendNumber(number) {
  // If calculation just finished, start fresh with the new number
  if (isCalculationFinished) {
    currentInput = number;
    equationTokens = [];
    isCalculationFinished = false;
    updateDisplay();
    return;
  }

  // Replace default "0" with the new digit, or append digit
  if (currentInput === "0") {
    currentInput = number;
  } else {
    // Limit to 16 digits to prevent display overflow
    if (currentInput.length < 16) {
      currentInput += number;
    }
  }

  updateDisplay();
}

/**
 * Appends a decimal point (.) if not already present
 */
function appendDecimal() {
  // If calculation just finished, start fresh as "0."
  if (isCalculationFinished) {
    currentInput = "0.";
    equationTokens = [];
    isCalculationFinished = false;
    updateDisplay();
    return;
  }

  // Check if current number already has a decimal
  if (!currentInput.includes(".")) {
    currentInput += ".";
    updateDisplay();
  }
}

/**
 * Handles operator selection (+, -, ×, ÷)
 */
function chooseOperator(operator) {
  // If screen shows an error message, reset before continuing
  if (currentInput === "Cannot divide by 0" || currentInput === "Error") {
    clearAll();
  }

  // If calculation just finished, use the result as the first operand
  if (isCalculationFinished) {
    equationTokens = [currentInput, operator];
    currentInput = "0";
    isCalculationFinished = false;
    updateDisplay();
    return;
  }

  // If user clicks a different operator consecutively, replace previous operator
  if (currentInput === "0" && equationTokens.length > 0) {
    equationTokens[equationTokens.length - 1] = operator;
    updateDisplay();
    return;
  }

  // Push current input number and chosen operator
  equationTokens.push(currentInput);
  equationTokens.push(operator);
  currentInput = "0";

  updateDisplay();
}

/**
 * Computes percentage (%) based on current context
 */
function calculatePercentage() {
  if (currentInput === "Cannot divide by 0" || currentInput === "Error") return;

  const currentVal = parseFloat(currentInput);
  if (isNaN(currentVal)) return;

  // If used in context like "100 + 10%", 10% of 100 = 10
  if (equationTokens.length >= 2) {
    const prevNumber = parseFloat(equationTokens[equationTokens.length - 2]);
    const operator = equationTokens[equationTokens.length - 1];

    if ((operator === "+" || operator === "-") && !isNaN(prevNumber)) {
      const percentageValue = (prevNumber * currentVal) / 100;
      currentInput = formatCalculatedNumber(percentageValue);
      updateDisplay();
      return;
    }
  }

  // Default: simply divide current number by 100
  const result = currentVal / 100;
  currentInput = formatCalculatedNumber(result);
  updateDisplay();
}

/**
 * Toggles positive and negative (+/-)
 */
function toggleSign() {
  if (currentInput === "0" || currentInput === "Cannot divide by 0" || currentInput === "Error") return;

  if (currentInput.startsWith("-")) {
    currentInput = currentInput.slice(1);
  } else {
    currentInput = "-" + currentInput;
  }

  updateDisplay();
}

/**
 * Deletes the last entered character (DEL)
 */
function deleteLast() {
  if (isCalculationFinished) {
    clearAll();
    return;
  }

  if (currentInput.length > 1) {
    currentInput = currentInput.slice(0, -1);
    // If only '-' remains, reset to "0"
    if (currentInput === "-") {
      currentInput = "0";
    }
  } else {
    currentInput = "0";
  }

  updateDisplay();
}

/**
 * Clears everything (AC - All Clear)
 */
function clearAll() {
  currentInput = "0";
  equationTokens = [];
  isCalculationFinished = false;
  displayExpression.textContent = "";
  displayPreview.textContent = "";
  updateDisplay();
}

// --- 4. Mathematical Evaluation (Order of Operations without eval) ---

/**
 * Evaluates tokens array following standard BODMAS / PEMDAS rule:
 * First pass: Multiplication (×) & Division (÷)
 * Second pass: Addition (+) & Subtraction (-)
 */
function evaluateExpression(tokens) {
  // Create a copy of the tokens array to avoid modifying the input
  let list = [...tokens];

  // --- Step 1: Solve all Multiplication (×) and Division (÷) ---
  let i = 0;
  while (i < list.length) {
    const token = list[i];
    if (token === "×" || token === "÷" || token === "*") {
      const prev = parseFloat(list[i - 1]);
      const next = parseFloat(list[i + 1]);

      if (isNaN(prev) || isNaN(next)) return "Error";

      let result = 0;
      if (token === "×" || token === "*") {
        result = prev * next;
      } else if (token === "÷") {
        // Prevent division by zero
        if (next === 0) {
          return "Cannot divide by 0";
        }
        result = prev / next;
      }

      // Replace [prev, operator, next] with calculated result
      list.splice(i - 1, 3, String(result));
      i = i - 1; // Move back one step after splice
    } else {
      i++;
    }
  }

  // --- Step 2: Solve all Addition (+) and Subtraction (-) ---
  i = 0;
  while (i < list.length) {
    const token = list[i];
    if (token === "+" || token === "-") {
      const prev = parseFloat(list[i - 1]);
      const next = parseFloat(list[i + 1]);

      if (isNaN(prev) || isNaN(next)) return "Error";

      let result = 0;
      if (token === "+") {
        result = prev + next;
      } else if (token === "-") {
        result = prev - next;
      }

      // Replace [prev, operator, next] with calculated result
      list.splice(i - 1, 3, String(result));
      i = i - 1; // Move back one step after splice
    } else {
      i++;
    }
  }

  const finalNumber = parseFloat(list[0]);
  if (isNaN(finalNumber)) return "Error";

  return formatCalculatedNumber(finalNumber);
}

/**
 * Rounds float calculation to eliminate IEEE-754 precision issues (e.g., 0.1 + 0.2 = 0.3)
 */
function formatCalculatedNumber(num) {
  // Precision up to 10 decimal places
  const rounded = Math.round(num * 10000000000) / 10000000000;
  return rounded.toString();
}

/**
 * Updates instant live preview of the calculation before '=' is pressed
 */
function updateLivePreview() {
  if (equationTokens.length > 0 && currentInput !== "Cannot divide by 0" && currentInput !== "Error") {
    const fullTokens = [...equationTokens, currentInput];
    const previewResult = evaluateExpression(fullTokens);

    if (previewResult !== "Error" && previewResult !== "Cannot divide by 0") {
      displayPreview.textContent = "= " + previewResult;
      return;
    }
  }
  displayPreview.textContent = "";
}

/**
 * Completes calculation on equal (=) button click
 */
function calculate() {
  // If no operation is queued, nothing to calculate
  if (equationTokens.length === 0) return;

  const fullTokens = [...equationTokens, currentInput];
  const equationString = fullTokens.join(" ");

  const result = evaluateExpression(fullTokens);

  if (result === "Cannot divide by 0") {
    displayExpression.textContent = equationString + " =";
    currentInput = "Cannot divide by 0";
    equationTokens = [];
    isCalculationFinished = true;
    displayPreview.textContent = "";
    displayMain.textContent = currentInput;
    return;
  }

  if (result === "Error") {
    currentInput = "Error";
    equationTokens = [];
    isCalculationFinished = true;
    displayMain.textContent = currentInput;
    return;
  }

  // Display completed equation and answer
  displayExpression.textContent = equationString + " =";
  currentInput = result;
  equationTokens = [];
  isCalculationFinished = true;
  displayPreview.textContent = "";

  // Add completed calculation to history
  addHistoryEntry(equationString, result);

  updateDisplay();
}

// --- 5. Extra Features: History, Copy & Themes ---

/**
 * Adds an equation and result to history array
 */
function addHistoryEntry(equation, result) {
  const now = new Date();
  const timeString = now.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });

  const item = {
    equation: equation,
    result: result,
    time: timeString
  };

  history.unshift(item); // Add to the top of history list

  // Limit stored history to last 30 items
  if (history.length > 30) {
    history.pop();
  }

  saveHistoryToStorage();
  renderHistory();

  // Show indicator dot on history icon if panel is currently hidden
  if (historyPanelContainer.classList.contains("d-none-custom")) {
    historyBadge.classList.remove("d-none");
  }
}

/**
 * Renders history items to the DOM
 */
function renderHistory() {
  historyList.innerHTML = "";

  if (history.length === 0) {
    historyList.innerHTML = `
      <div class="history-empty text-center py-5 text-muted">
        <i class="bi bi-journal-x fs-1 d-block mb-2 opacity-50"></i>
        <p class="mb-0 fw-medium">No calculations yet</p>
        <small class="opacity-75">Your completed calculations will appear here.</small>
      </div>
    `;
    return;
  }

  history.forEach(function (item) {
    const card = document.createElement("div");
    card.className = "history-item";
    card.title = "Click to load this calculation into the calculator";
    card.innerHTML = `
      <div class="d-flex justify-content-between align-items-center">
        <div class="history-item-equation">${item.equation}</div>
        <div class="history-item-time">${item.time}</div>
      </div>
      <div class="history-item-result">= ${item.result}</div>
    `;

    // Click history entry to restore calculation value
    card.addEventListener("click", function () {
      currentInput = item.result;
      equationTokens = [];
      isCalculationFinished = false;
      displayExpression.textContent = item.equation + " =";
      updateDisplay();
    });

    historyList.appendChild(card);
  });
}

/**
 * Clears all calculation history
 */
function clearHistory() {
  history = [];
  saveHistoryToStorage();
  renderHistory();
  historyBadge.classList.add("d-none");
}

/**
 * Saves history to browser localStorage
 */
function saveHistoryToStorage() {
  try {
    localStorage.setItem("ai_calc_history", JSON.stringify(history));
  } catch (e) {
    // Graceful fallback if storage is disabled
  }
}

/**
 * Loads history from browser localStorage
 */
function loadHistoryFromStorage() {
  try {
    const saved = localStorage.getItem("ai_calc_history");
    if (saved) {
      history = JSON.parse(saved);
      renderHistory();
    }
  } catch (e) {
    history = [];
  }
}

/**
 * Toggles calculation history panel visibility
 */
function toggleHistoryPanel() {
  historyPanelContainer.classList.toggle("d-none-custom");
  historyBadge.classList.add("d-none");
}

/**
 * Copies current displayed number to clipboard
 */
function copyResult() {
  const textToCopy = currentInput;
  if (!textToCopy || textToCopy === "Error" || textToCopy === "Cannot divide by 0") return;

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(textToCopy).then(showCopyAlert);
  } else {
    // Fallback for browsers without Clipboard API
    const textarea = document.createElement("textarea");
    textarea.value = textToCopy;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);
    showCopyAlert();
  }
}

/**
 * Shows temporary "Copied to clipboard!" alert badge
 */
function showCopyAlert() {
  copyAlert.classList.add("show");
  setTimeout(function () {
    copyAlert.classList.remove("show");
  }, 1600);
}

/**
 * Toggles Dark & Light mode
 */
function toggleTheme() {
  const body = document.body;
  const isLight = body.classList.toggle("theme-light");
  body.classList.toggle("theme-dark", !isLight);

  // Set Bootstrap HTML data attribute
  document.documentElement.setAttribute("data-bs-theme", isLight ? "light" : "dark");

  // Update theme toggle icon
  if (isLight) {
    themeIcon.className = "bi bi-moon-stars-fill";
    localStorage.setItem("ai_calc_theme", "light");
  } else {
    themeIcon.className = "bi bi-sun-fill";
    localStorage.setItem("ai_calc_theme", "dark");
  }
}

/**
 * Loads saved theme preference from localStorage
 */
function loadSavedTheme() {
  const savedTheme = localStorage.getItem("ai_calc_theme");
  if (savedTheme === "light") {
    document.body.classList.add("theme-light");
    document.body.classList.remove("theme-dark");
    document.documentElement.setAttribute("data-bs-theme", "light");
    themeIcon.className = "bi bi-moon-stars-fill";
  } else {
    document.body.classList.add("theme-dark");
    document.body.classList.remove("theme-light");
    document.documentElement.setAttribute("data-bs-theme", "dark");
    themeIcon.className = "bi bi-sun-fill";
  }
}

// --- 6. Event Listeners & Button Interactions ---

// Handle Button Clicks
allButtons.forEach(function (button) {
  button.addEventListener("click", function () {
    const number = button.getAttribute("data-number");
    const operator = button.getAttribute("data-operator");
    const action = button.getAttribute("data-action");

    if (number !== null) {
      appendNumber(number);
    } else if (operator !== null) {
      chooseOperator(operator);
    } else if (action !== null) {
      if (action === "clear") clearAll();
      else if (action === "delete") deleteLast();
      else if (action === "decimal") appendDecimal();
      else if (action === "calculate") calculate();
      else if (action === "percent") calculatePercentage();
      else if (action === "toggle-sign") toggleSign();
    }
  });
});

// Flash button active state for keyboard press
function flashButtonByKey(keyName) {
  let matchedButton = null;
  allButtons.forEach(function (btn) {
    if (btn.getAttribute("data-key") === keyName) {
      matchedButton = btn;
    }
  });

  if (matchedButton) {
    matchedButton.classList.add("keyboard-active");
    setTimeout(function () {
      matchedButton.classList.remove("keyboard-active");
    }, 150);
  }
}

// Keyboard Support
window.addEventListener("keydown", function (e) {
  const key = e.key;

  // Digits (0 - 9)
  if (!isNaN(key) && key !== " ") {
    flashButtonByKey(key);
    appendNumber(key);
    return;
  }

  // Decimal Point
  if (key === "." || key === ",") {
    flashButtonByKey(".");
    appendDecimal();
    return;
  }

  // Operators (+, -, *, /)
  if (key === "+") {
    flashButtonByKey("+");
    chooseOperator("+");
  } else if (key === "-") {
    flashButtonByKey("-");
    chooseOperator("-");
  } else if (key === "*" || key.toLowerCase() === "x") {
    flashButtonByKey("*");
    chooseOperator("×");
  } else if (key === "/") {
    e.preventDefault(); // Prevent default browser shortcut
    flashButtonByKey("/");
    chooseOperator("÷");
  } else if (key === "%") {
    flashButtonByKey("%");
    calculatePercentage();
  } else if (key === "±" || key === "F9") {
    flashButtonByKey("±");
    toggleSign();
  }

  // Calculate (Enter or =)
  if (key === "Enter" || key === "=") {
    e.preventDefault();
    flashButtonByKey("Enter");
    calculate();
  }

  // Delete last character (Backspace)
  if (key === "Backspace") {
    flashButtonByKey("Backspace");
    deleteLast();
  }

  // Clear all (Escape or 'c' / 'C')
  if (key === "Escape" || key.toLowerCase() === "c") {
    flashButtonByKey("Escape");
    clearAll();
  }
});

// Action button event listeners
copyBtn.addEventListener("click", copyResult);
themeToggleBtn.addEventListener("click", toggleTheme);
historyToggleBtn.addEventListener("click", toggleHistoryPanel);
clearHistoryBtn.addEventListener("click", clearHistory);

// Initialize saved state on page load
loadSavedTheme();
loadHistoryFromStorage();
updateDisplay();
