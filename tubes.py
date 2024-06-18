import streamlit as st
import string

# Set page title and favicon
st.set_page_config(page_title="Tugas Besar TBA", page_icon="✍")

# Custom CSS for styling with Poppins font and white background for profile images
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    body {
        font-family: 'Poppins', sans-serif;
    }

    .title {
        font-family: 'Poppins', sans-serif;
        font-weight: bold;
        font-size: 3rem;
        color: #492bc2;
        text-align: center;
        margin-bottom: 20px;
    }

    .input-area {
        margin-top: 30px;
        text-align: center;
    }

    .output-area {
        margin-top: 30px;
        text-align: left;
    }

    .stTextInput > div > div > input {
        border-radius: 10px;
        padding: 10px;
        font-size: 1.2rem;
    }

    .stButton > button {
        background-color: #492bc2;
        color: white;
        padding: 10px 20px;
        font-size: 1.2rem;
        border-radius: 10px;
        border: none;
        cursor: pointer;
    }

    .stButton > button:hover {
        background-color: #492bc2;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page title
st.markdown("<div class='title'>Memeriksa Kevalidan Struktur Kalimat</div>", unsafe_allow_html=True)

# Input area
st.markdown("<div class='input-area'>", unsafe_allow_html=True)
input_text = st.text_input("Masukkan kalimat Anda di sini:")
if st.button("Submit"):
    if input_text:
        # Token recognizer function
        def tokenrecognizer(sentence):
            token = sentence.split()
            pola = []
            for word in token:
                result = recognize(word)
                if result == 'acceptedAsSubject':
                    pola.append('S')
                elif result == 'acceptedAsPredikat':
                    pola.append('P')
                elif result == 'acceptedAsObject':
                    pola.append('O')
                elif result == 'acceptedAsKeterangan':
                    pola.append('K')
                else:
                    pola.append('tidak valid')  # Menambahkan 'tidak valid' jika tidak dikenali
            return pola

        # Recognize function
        def recognize(word):
            alphabet = list(string.ascii_lowercase)
            state = [f'q{i}' for i in range(1, 71)]
            transisi = {}
            for s in state:
                for a in alphabet:
                    transisi[(s, a)] = 'error'
                transisi[(s, '#')] = 'error'
                transisi[(s, ' ')] = 'error'

            transisi[("q1", " ")] = "q1"
            transisi[("q5", "#")] = "acceptedAsSubject"
            transisi[("q5", " ")] = "acceptedAsSubject"
            transisi[("q21", "#")] = "acceptedAsPredikat"
            transisi[("q21", " ")] = "acceptedAsPredikat"
            transisi[("q40", "#")] = "acceptedAsObject"
            transisi[("q40", " ")] = "acceptedAsObject"
            transisi[("q55", "#")] = "acceptedAsKeterangan"
            transisi[("q55", " ")] = "acceptedAsKeterangan"

            # HURUF AWAL
            transisi[("q1", "s")] = "q2"
            transisi[("q1", "k")] = "q6"
            transisi[("q1", "d")] = "q9"
            transisi[("q1", "m")] = "q11"
            transisi[("q1", "b")] = "q31"
            transisi[("q1", "l")] = "q56"
            transisi[("q1", "n")] = "q37"
            transisi[("q1", "t")] = "q61"
            transisi[("q1", "p")] = "q64"
            transisi[("q1", "g")] = "q41"
            transisi[("q1", "a")] = "q51"

            # SUBJEK
            #saya
            transisi[("q2", "a")] = "q3"
            transisi[("q3", "y")] = "q4"
            transisi[("q4", "a")] = "q5"
            #kamu
            transisi[("q6", "a")] = "q7"
            transisi[("q7", "m")] = "q8"
            transisi[("q8", "u")] = "q5"
            #kita
            transisi[("q6", "i")] = "q16"
            transisi[("q16", "t")] = "q17"
            transisi[("q17", "a")] = "q5"
            #dia
            transisi[("q9", "i")] = "q10"
            transisi[("q10", "a")] = "q5"
            #mereka
            transisi[("q11", "e")] = "q12"
            transisi[("q12", "r")] = "q13"
            transisi[("q13", "e")] = "q14"
            transisi[("q14", "k")] = "q15"
            transisi[("q15", "a")] = "q5"

            # PREDIKAT
            #makan
            transisi[("q11", "a")] = "q18"
            transisi[("q18", "k")] = "q19"
            transisi[("q19", "a")] = "q20"
            transisi[("q20", "n")] = "q21"
            #melihat
            transisi[("q11", "e")] = "q12"
            transisi[("q12", "l")] = "q25"
            transisi[("q25", "i")] = "q26"
            transisi[("q26", "h")] = "q27"
            transisi[("q27", "a")] = "q28"
            transisi[("q28", "t")] = "q21"
            #minum
            transisi[("q11", "i")] = "q22"
            transisi[("q22", "n")] = "q23"
            transisi[("q23", "u")] = "q24"
            transisi[("q24", "m")] = "q21"
            #masak
            transisi[("q11", "a")] = "q18"
            transisi[("q18", "s")] = "q29"
            transisi[("q29", "a")] = "q30"
            transisi[("q30", "k")] = "q21"
            #bermain
            transisi[("q31", "e")] = "q32"
            transisi[("q32", "r")] = "q33"
            transisi[("q33", "m")] = "q34"
            transisi[("q34", "a")] = "q35"
            transisi[("q35", "i")] = "q36"
            transisi[("q36", "n")] = "q21"

            # OBJEK
            #nasi
            transisi[("q37", "a")] = "q38"
            transisi[("q38", "s")] = "q39"
            transisi[("q39", "i")] = "q40"
            #air
            transisi[("q51", "i")] = "q52"
            transisi[("q52", "r")] = "q40"
            #gulai
            transisi[("q41", "u")] = "q42"
            transisi[("q42", "l")] = "q43"
            transisi[("q43", "a")] = "q44"
            transisi[("q44", "i")] = "q40"
            #gedung
            transisi[("q41", "e")] = "q47"
            transisi[("q47", "d")] = "q48"
            transisi[("q48", "u")] = "q49"
            transisi[("q49", "n")] = "q50"
            transisi[("q50", "g")] = "q40"
            #game
            transisi[("q41", "a")] = "q45"
            transisi[("q45", "m")] = "q46"
            transisi[("q46", "e")] = "q40"

            # KETERANGAN
            #tadi
            transisi[("q61", "a")] = "q62"
            transisi[("q62", "d")] = "q63"
            transisi[("q63", "i")] = "q55"
            #besok
            transisi[("q31", "e")] = "q32"
            transisi[("q32", "s")] = "q53"
            transisi[("q53", "o")] = "q54"
            transisi[("q54", "k")] = "q55"
            #lusa
            transisi[("q56", "u")] = "q57"
            transisi[("q57", "s")] = "q58"
            transisi[("q58", "a")] = "q55"
            #nanti
            transisi[("q37", "a")] = "q38"
            transisi[("q38", "n")] = "q59"
            transisi[("q59", "t")] = "q60"
            transisi[("q60", "i")] = "q55"
            #perlahan
            transisi[("q64", "e")] = "q65"
            transisi[("q65", "r")] = "q66"
            transisi[("q66", "l")] = "q67"
            transisi[("q67", "a")] = "q68"
            transisi[("q68", "h")] = "q69"
            transisi[("q69", "a")] = "q70"
            transisi[("q70", "n")] = "q55"

            current_state = 'q1'
            word = word + '#'  # Tambahkan simbol akhir
            for char in word:
                current_state = transisi.get((current_state, char), 'error')
                if current_state == 'error':
                    return 'error'
            return current_state
        
        def parser(sentence):
            pola = tokenrecognizer(sentence)
            stack = ['#', 'Kalimat']
            idx = 0
            result = f"Struktur kalimat: {[p for p in pola if p != 'TIDAK VALID']}"
            valid = True

            while len(stack) > 0:
                top = stack.pop()
                
                if top in ['S', 'P', 'O', 'K', '#']:
                    if idx < len(pola) and top == pola[idx]:
                        idx += 1
                    elif top == '#' and idx == len(pola):
                        pass  # Kalimat valid, tidak perlu tambahan pesan
                    else:
                        result = f"Struktur kalimat: {[p for p in pola if p != 'TIDAK VALID']}"
                        result += "\nPARSER: Kalimat tidak valid."
                        valid = False
                        break
                elif top == 'Kalimat':
                    if 'K' in pola and 'O' in pola:
                        stack.extend(['S', 'P', 'O', 'K'][::-1])
                    elif 'K' in pola:
                        stack.extend(['S', 'P', 'K'][::-1])
                    elif 'O' in pola:
                        stack.extend(['S', 'P', 'O'][::-1])
                    else:
                        stack.extend(['S', 'P'][::-1])

            if idx != len(pola):
                result = f"Struktur kalimat: {[p for p in pola if p != 'TIDAK VALID']}"
                result += "\nPARSER: Kalimat tidak valid."
                valid = False

            if valid:
                result += "\nPARSER: Kalimat valid."

            return result

        # Process the input sentence and display the result (updated)
        result = parser(input_text)
        st.markdown("<div class='output-area'>", unsafe_allow_html=True)
        st.markdown(result.replace("\n", "<br>"), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)