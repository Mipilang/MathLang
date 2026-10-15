<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tradutor MathLang</title>
    <style>
        body { font-family: sans-serif; background: #121212; color: #fff; padding: 20px; text-align: center; }
        textarea { width: 90%; max-width: 500px; height: 100px; margin: 10px 0; padding: 10px; background: #222; color: #fff; border: 1px solid #444; border-radius: 8px; font-size: 16px; }
        #resultado { margin-top: 20px; font-size: 24px; color: #00ffcc; font-weight: bold; min-height: 40px; }
    </style>
</head>
<body>
    <h1>📐 Tradutor Universal MathLang</h1>
    <p>Escreve em português para converter em símbolos:</p>
    <textarea id="entrada" placeholder="Ex: Minha mente está crescendo..." oninput="traduzir()"></textarea>
    <div id="resultado"></div>

    <script>
        const radicaisMatematicos = {
            "eu": "1", "voc": "2", "outr": "2", "nos": "1+2",
            "nad": "0", "vazi": "0", "zero": "0", "um": "1", "dois": "2",
            "nao": "-", "nunc": "-", "jama": "-", "sim": "+", "com": "+",
            "sou": "=", "e": "=", "est": "=", "som": "=======",
            "muit": "×", "mais": "×", "grand": "×",
            "ment": "θ", "pens": "θ", "segr": "θ",
            "idei": "λ", "luz": "λ", "insp": "λ",
            "fim": "Ω", "dest": "Ω", "conc": "Ω",
            "evol": "e", "cres": "e", "melh": "e", "natu": "e", "vida": "e",
            "mud": "Δ", "viaj": "Δ", "mov": "Δ",
            "fam": "√", "orig": "√", "base": "√",
            "semp": "∞", "infi": "∞", "eter": "∞",
            "grup": "∑", "soci": "∑", "povo": "∑",
            "temp": "∫", "acum": "∫", "apre": "∫",
            "meu": "%", "minh": "%", "seu": "%", "teu": "%",
            "fut": ">", "avan": ">", "pass": "<", "atras": "<"
        };

        function limparTexto(texto) {
            return texto.toLowerCase()
                .normalize("NFD").replace(/[\u0300-\u036f]/g, "") // Remove acentos
                .replace(/[.,\/#!\$%\^&\*;:{}=\-_`~()!?]/g, ""); // Remove pontuação
        }

        function traduzir() {
            const input = document.getElementById("entrada").value;
            const palavras = limparTexto(input).split(/\s+/);
            let resultado = [];

            for (let palavra of palavras) {
                if (!palavra) continue;
                let traduzida = false;

                for (let radical in radicaisMatematicos) {
                    if (palavra.startsWith(radical)) {
                        resultado.push(radicaisMatematicos[radical]);
                        traduzida = true;
                        break;
                    }
                }

                if (!traduzida) {
                    resultado.push(`[x:${palavra}]`);
                }
            }

            document.getElementById("resultado").innerText = resultado.join(" ");
        }
    </script>
</body>
</html>
