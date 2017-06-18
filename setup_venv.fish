# create an activation function
function activate
    set -gx USER_PATH $PATH
    set -gx VENV_PROMPT "(venv)"
    set -gx PATH $PWD/venv/bin /usr/local/sbin /usr/local/bin /usr/sbin /usr/bin /sbin /bin
end

# create a deactivate function
function deactivate
    set -gx PATH $USER_PATH
    set -e USER_PATH
    set -e VENV_PROMPT
end
       
# setup the virtual environment
conda create -y -p ./venv \
    python=3.6 \
    numpy      \
    scipy      \
    h5py       \
    ipython    \
    matplotlib

# activate the environment
activate
