[ -f packages.txt ] &&
sudo apt update &&
sudo apt upgrade -y &&
sudo xargs apt install -y <packages.txt;

[ -f pyproject.toml ] &&
pip3 install --user poetry &&
poetry install &&
echo '✅ Packages and dependencies installed!';