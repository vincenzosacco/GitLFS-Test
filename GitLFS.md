# Come Caricare File di Grandi Dimensioni su GitHub Usando Git LFS

## Passo 1: Installa Git LFS
- Scarica e installa Git LFS dal sito ufficiale: https://git-lfs.github.com/
- Dopo l'installazione, esegui il seguente comando per inizializzare Git LFS nel tuo repository:
  ``` shell
  git lfs install
  ```

## Passo 2: Traccia il File di Grandi Dimensioni
- Vai nella cartella del tuo repository tramite terminale.
- Usa il seguente comando per tracciare il file di grandi dimensioni:
  ``` shell
  git lfs track "nomefile.ext"
  ```
  è anche possibile tracciare tutti i file con una certa estensione:
  ``` shell
  git lfs track "*.ext"
  ```

- Questo comando crea un file `.gitattributes` nel tuo repository che indica a Git di usare LFS per il file specificato.

## Passo 3: Aggiungi il File di Grandi Dimensioni
- Aggiungi il file al tuo repository con il comando:
  ```
  git add nomefile.ext
  ```

## Passo 4: Effettua il Commit delle Modifiche
- Effettua il commit delle modifiche con un messaggio descrittivo:
  ```
  git commit -m "Aggiunta nomefile.ext (large file)"
  ```

## Passo 5: Esegui il Push su GitHub
- Infine, esegui il push delle modifiche sul repository GitHub:
  ```
  git push origin main
  ```
- Sostituisci `main` con il nome del tuo branch se ne stai usando uno diverso.

## Passo 6: Verifica il Caricamento
- Vai sul tuo repository GitHub tramite browser e verifica che il file sia stato caricato correttamente.

## Note Aggiuntive
- Il [comando di tracciamento](#passo-2-traccia-il-file-di-grandi-dimensioni) deve essere eseguito prima di [aggiungere il file](#passo-3-aggiungi-il-file-di-grandi-dimensioni) ed [effettuare il commit](#passo-4-effettua-il-commit-delle-modifiche).

- Tieni presente i [limiti di spazio e banda associati](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-storage-and-bandwidth-usage) a Git LFS su GitHub.