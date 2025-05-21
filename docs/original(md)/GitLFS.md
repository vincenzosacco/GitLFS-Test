# Come Caricare File di Grandi Dimensioni su GitHub Usando Git LFS

## 1. Installare Git LFS

Prima di tutto, assicurati che Git LFS sia installato sul tuo sistema. Puoi installarlo da [sito ufficiale](https://git-lfs.github.com/) o utilizzare un package manager.

- Per Windows (usando Chocolatey): `choco install git-lfs`
- Per macOS: `brew install git-lfs`
- Per Linux: `sudo apt install git-lfs` (Ubuntu/Debian) o simili per la tua distribuzione.

Dopo l'installazione, inizializza Git LFS:
```bash
# Inizializza Git LFS a livello globale
git lfs install
```
```bash
# Inizializza Git LFS solo per il repository corrente
git lfs install --local
```

## 2. Tracciare File di Grandi Dimensioni
A questo punto :
- Se il file *non è ancora presente in un commit*, è possibile seguire sia le istruzioni [metodo 'track'](_steps-track.md).
  
- Se il file *è già presente in un commit* , bisogna scegliere
    - se si vuole **riscrivere la cronologia dei commit**, seguire [metodo 'migrate rewrite'](_steps-rewrite.md).
    - se **non si vuole riscrivere la cronologia dei commit**, seguire [metodo 'migrate no-rewrite'](_steps-norewrite.md).
  
***NOTA*** - Se la tua intenzione è quella caricare su GitHub una repo che contiene già file più grandi di 100MB, allora devi necessariamente seguire il [metodo 'migrate rewrite'](_steps-rewrite.md).


## Note Aggiuntive
- Tieni presente i [limiti di spazio e banda associati](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-storage-and-bandwidth-usage) a Git LFS su GitHub, e [monitora l'utilizzo del tuo spazio](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-git-large-file-storage/viewing-your-git-large-file-storage-usage).
- Anche chi clona la repo deve eseguire [Installare Git LFS](#1-installare-git-lfs)
- Per clonare la repo che utilizza GitLFS usare `git lfs clone`
- Se la repo è già clonata da prima che fosse abilitato LFS, utilizzare  `git lfs pull`

  
<!-- TROUBLESHOOTING -->
# Troubleshooting
In ogni caso rimando alle [FAQs della documentazione ufficiale](https://github.com/git-lfs/git-lfs/blob/main/docs/man/git-lfs-faq.adoc)

### Ho clonato la repo ma non trovo i file di grandi dimensioni.
  1. Assicurati di avere installato Git LFS e di aver eseguito `git lfs install`.
  2. Prova a eseguire `git lfs pull` per scaricare i file di grandi dimensioni.
  


