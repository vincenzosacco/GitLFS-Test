# Come Caricare File di Grandi Dimensioni su GitHub Usando Git LFS - versione 'Manuale'

### Passo 1: Traccia il File di Grandi Dimensioni
1. Vai nella cartella del tuo repository tramite terminale.
2. Per tracciare un file di grandi dimensioni, i comandi variano a seconda che il file sia già presente nel repository o meno:
    
    - Se il file *non è ancora presente in un commit*, puoi usare:
      ``` shell
      git lfs track "nomefile.ext"
      ```
      è anche possibile tracciare tutti i file con una certa estensione:
      ``` shell
      git lfs track "*.ext"
      ```

     - Se il file *è già presente in un commit*
      TODo
     

3. I comandi precedenti creano un file *.gitattributes* nel tuo repository che indica a Git di usare LFS per il file specificato. Aggiungi questo file al working tree se non è già presente:
    ``` shell
    git add .gitattributes
    ```

*Per verificare quali file sono tracciati da LFS, puoi usare il comando:*
``` shell
git lfs ls-files
```

### Passo 2: Aggiungi il File di Grandi Dimensioni
- Aggiungi il file al tuo repository con il comando:
    ``` shell
    git add nomefile.ext
    
    # Se hai usato <git lfs track> per tracciare file già presenti nella repo
    git add --renormalize .
    ```
    *`--renormalize` [motivo](https://github.com/git-lfs/git-lfs/blob/main/docs/man/git-lfs-faq.adoc#file-size)*

### Passo 3: Effettua il Commit delle Modifiche
-  Esegui il commit delle modifiche:
    ``` shell
      git commit -m "Aggiunta nomefile.ext (large file)"
    ```

### Passo 4: Esegui il Push su GitHub
- Infine, esegui il push delle modifiche sul repository GitHub:
  ```shell
  git push
  ```

