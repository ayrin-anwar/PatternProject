 function ShowHideDiv() {
            var translate = document.getElementById("translate");
            var translate_text_box = document.getElementById("translate_text_box");
            translate_text_box.style.display = translate.checked ? "block" : "none";

             var ocr = document.getElementById("ocr");
             var ocr_input = document.getElementById("ocr_input");
            ocr_input.style.display = ocr.checked ? "block" : "none";

            var ocr_translate = document.getElementById("ocr_translate");
             var ocr_translate_input = document.getElementById("ocr_translate_input");
            ocr_translate_input.style.display = ocr_translate.checked ? "block" : "none";
        }
