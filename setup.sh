rm -r -f setup_files
mkdir setup_files
cd setup_files || return
git clone --depth 1 https://github.com/testdevlab/TestRay.git
cd testray || return
rake install --trace