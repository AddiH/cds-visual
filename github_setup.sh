# in case cloud forgot
git config --global user.email “astrid.elmann@gmail.com”
git config --global user.name “AddiH”

# in case the local you are working on is outdated (if you’re switching between local, cloud and worker 02)
git pull

# pull from main
git checkout -b CDS-AU-DK-main main
git config pull.rebase false
git pull https://github.com/CDS-AU-DK/cds-visual.git main

# make changes
git checkout main
git merge --no-ff CDS-AU-DK-main
git push origin main