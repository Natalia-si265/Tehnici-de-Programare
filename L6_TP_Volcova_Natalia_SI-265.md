# Laboratorul 6 GitHub pas cu pas

Nume și prenume: Volcova Natalia  
Grupa: SI-265  
Username GitHub: Natalia-si265

## Depozite

- https://github.com/Natalia-si265/exercitiu-git
- https://github.com/Natalia-si265/exercitiu-2
- Depozitul disciplinei: https://github.com/Natalia-si265/Tehnici-de-Programare

## Pașii A1–A10

A1. A fost folosit contul existent Natalia-si265, autentificat pe GitHub.

A2. A fost verificată instalarea Git 2.53.0 și au fost configurate global numele Volcova Natalia, adresa asociată contului, ramura implicită main și pull.rebase=false.

A3. Am creat pe GitHub depozitul public exercitiu-git, cu fișierul README.md.

A4. Depozitul a fost adus pe calculator prin git clone.

A5. A fost creat salut.py cu print("Salut, GitHub!"), rulat și salvat prin git add și git commit, cu mesajul Adaug salut.py.

A6. Commit-ul a fost trimis pe GitHub prin git push, iar fișierul apare în depozit.

A7. Am adăugat în README, din editorul GitHub, rândul Aici exersez git.; modificarea a fost adusă local prin git pull, cu rezultat Fast-forward.

A8. A fost creat mediul .venv, apoi fișierul .gitignore cu regulile .venv/ și __pycache__/; git check-ignore a confirmat ignorarea mediului, iar regula a fost salvată și trimisă prin commit și push.

A9. Istoricul a fost citit cu git log --oneline; un al doilea print adăugat temporar în salut.py a fost verificat cu git diff și eliminat cu git restore, după care copia locală a rămas fără modificări.

A10. Depozitul exercitiu-2 a fost inițializat local cu git init, a fost creat README.md și primul commit, apoi depozitul a fost publicat prin git push -u origin main.

## Rezultate

Rularea python salut.py a afișat:

```text
Salut, GitHub!
```

Istoricul depozitului exercitiu-git:

```text
ebba37b Add description to README
083c17f Ignor mediul virtual
e1db647 Adaug salut.py
f711b5c Initial commit
```

Depozitul conține README.md, salut.py și .gitignore. Are patru commit-uri și este public.

Istoricul depozitului exercitiu-2:

```text
3780fed Primul commit
```

Depozitul conține README.md și este public. Ramura main urmărește origin/main.

După sincronizare, git status în exercitiu-git a afișat:

```text
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

## Concluzii

Git păstrează istoricul local al proiectului. git add pregătește modificările, git commit le salvează în istoric, git push le trimite pe GitHub, iar git pull aduce modificările de pe GitHub. .gitignore exclude fișierele care nu trebuie urmărite. git diff arată modificările nesalvate în commit, iar git restore readuce un fișier la versiunea salvată.

## Surse și ajutor

Fișa L6_Laborator_GitHub_pas_cu_pas.docx. ChatGPT a ajutat la pregătirea fișierelor, configurarea și executarea comenzilor Git și redactarea raportului. Crearea depozitelor și editarea README pe GitHub au fost făcute manual.
