
        function copyToClipboard() {
            /* Get the text field */
            var copyText = document.getElementById("output_text");

            /* Select the text field */
            copyText.select();
            copyText.setSelectionRange(0, 99999); /* For mobile devices */

            /* Copy the text inside the text field */
            document.execCommand("copy");

            /* Alert the copied text */
            alert("Copied the text: " + copyText.value);
        }

        function selectLanguage(language, inputType) {
            // 선택된 언어를 표시하는 span 업데이트
            if (inputType === 'source') {
                document.getElementById('selectedSourceLanguage').innerText = language;
                document.getElementById('sourceLanguageInput').value = language;
            } else if (inputType === 'target') {
                document.getElementById('selectedTargetLanguage').innerText = language;
                document.getElementById('targetLanguageInput').value = language;
            }
        }

        window.addEventListener("load", ()=> {
        const loader = document.querySelector(".loader");

        loader.classList.add("loader—hidden");
        loader.addEventListener("transitionend", ()=> {
        document.body.removeChild(loader);
    });
});
const dropdowns = document.querySelectorAll('.dropdown');

dropdowns.forEach(dropdown => {
    const select = dropdown.querySelector('.select');
    const caret = dropdown.querySelector('.caret');
    const menu = dropdown.querySelector('.menu');
    const options = dropdown.querySelectorAll('.menu li');
    const selected = dropdown.querySelector('.selected');

    select.addEventListener('click', () => {
        select.classList.toggle('select-clicked');
        caret.classList.toggle('caret-rotate');
        menu.classList.toggle('menu-open');

    });

    options.forEach(option => {
        option.addEventListener('click', () => {
            selected.innerText = option.innerText;
            select.classList.remove('select-clicked');
            caret.classList.remove('caret-rotate');
            menu.classList.remove('menu-open');

            options.forEach(option => {
                option.classList.remove('active');
            });

            option.classList.add('active');
        });
    });
});

function toggleAccordion(panelId) {
            var panel = document.getElementById(panelId);
            panel.style.display = (panel.style.display === 'block') ? 'none' : 'block';
        }

 function openPopup() {
    document.getElementById('popup').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
  }

  function closePopup() {
    document.getElementById('popup').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
  }