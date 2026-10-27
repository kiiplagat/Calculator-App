<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Calculator</title>
<style>
  body { background:#1a1a1a; margin:0; min-height:100vh; display:flex; justify-content:center; align-items:center; font-family:sans-serif; }
  .calc { width:320px; padding:10px; }
  #display { width:100%; box-sizing:border-box; background:#000; color:#fff; border:none; font-size:36px; text-align:right; padding:14px; margin-bottom:10px; }
  .grid { display:grid; grid-template-columns:repeat(4,1fr); gap:10px; }
  button { background:#333; color:#fff; border:none; font-size:24px; padding:18px 0; border-radius:4px; cursor:pointer; }
  button:active { background:#555; }
  #equals { grid-column:1 / -1; background:#0099ff; font-size:28px; }
</style>
</head>
<body>
<div class="calc">
  <input id="display" readonly>
  <div class="grid" id="grid"></div>
</div>
<script>
  const display = document.getElementById('display');
  const grid = document.getElementById('grid');
  const keys = ["C","⌫","%","/","7","8","9","*","4","5","6","-","1","2","3","+","0",".","x²","√"];

  function evaluate(expr) {
    if (!/^[0-9+\-*/.() ]+$/.test(expr)) throw new Error("bad input");
    const result = Function('"use strict"; return (' + expr + ')')();
    if (!isFinite(result)) throw new Error("math error");
    return result;
  }

  function press(k) {
    try {
      if (k === "C") display.value = "";
      else if (k === "⌫") display.value = display.value.slice(0, -1);
      else if (k === "x²") display.value = evaluate(display.value) ** 2;
      else if (k === "√") display.value = Math.sqrt(evaluate(display.value));
      else if (k === "%") display.value = evaluate(display.value) / 100;
      else if (k === "=") display.value = evaluate(display.value);
      else display.value += k;
    } catch (e) {
      display.value = "Error";
    }
  }

  [...keys, "="].forEach(k => {
    const b = document.createElement('button');
    b.textContent = k;
    if (k === "=") b.id = "equals";
    b.onclick = () => press(k);
    grid.appendChild(b);
  });
</script>
</body>
</html>
