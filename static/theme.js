(function () {
    var storageKey = "theme";
    var buttonId = "theme-toggle-global";
    var iconMoon = "fas fa-moon";
    var iconSun = "fas fa-sun";

    function setTheme(theme) {
        if (theme === "dark") {
            document.body.setAttribute("data-theme", "dark");
        } else {
            document.body.removeAttribute("data-theme");
        }
        localStorage.setItem(storageKey, theme);
        updateButton(theme);
    }

    function currentTheme() {
        return document.body.getAttribute("data-theme") === "dark" ? "dark" : "light";
    }

    function updateButton(theme) {
        var btn = document.getElementById(buttonId);
        if (!btn) return;

        var isDark = theme === "dark";
        var icon = btn.querySelector("i");
        var text = btn.querySelector("span");
        if (icon) icon.className = isDark ? iconSun : iconMoon;
        if (text) text.textContent = isDark ? "Modo Claro" : "Modo Escuro";
    }

    function createButton() {
        if (document.getElementById(buttonId)) return;

        var btn = document.createElement("button");
        btn.id = buttonId;
        btn.className = "theme-switch-floating";
        btn.type = "button";
        btn.innerHTML = '<i class="fas fa-moon"></i><span>Modo Escuro</span>';
        btn.addEventListener("click", function () {
            var next = currentTheme() === "dark" ? "light" : "dark";
            setTheme(next);
        });
        document.body.appendChild(btn);
    }

    function initialTheme() {
        var saved = localStorage.getItem(storageKey);
        if (saved === "dark" || saved === "light") return saved;
        if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
            return "dark";
        }
        return "light";
    }

    document.addEventListener("DOMContentLoaded", function () {
        createButton();
        setTheme(initialTheme());
    });
})();
