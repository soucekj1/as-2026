
SP1 Kroužky

Kód žíka:20

Tři chybné věci: 1. Některé kroužky jsou napsané s prvním písmem malým.
                  2. U některých tříd je mezera meti IT a 2
                  3. Dnz v týdnu nejsou všechny napsané špatně, neboli některé zkratkově a některé plným názvem


prihlasky: PK id_prihlasky, FK id_zaka → zaci, FK id_krouzku → krouzky.

Zaci: PK id_zaka, FK id_prihlaska → prihlasky, FK id_krouzku → krouzky

krouzky: PK id_krozku, FK id_prihlasky → prihlaska, FK id_zaka → Zaci

<img width="2562" height="2970" alt="Mermaid Flow Flow-2026-10-12-122416" src="https://github.com/user-attachments/assets/50f7aca2-bc63-4cca-849d-cccf3919f3e1" />
