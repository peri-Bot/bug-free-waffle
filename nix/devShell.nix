{ pkgs }:

let
  python-env = pkgs.python311.withPackages (ps: with ps; [
    telethon
    numpy
    pandas
  ]);
in
pkgs.mkShell {
  buildInputs = [ python-env ];

  shellHook = ''
    if [[ ! -d .venv ]]; then
      echo "Creating a new virtual environment using Nix-managed Python 3.11..."
      ${python-env}/bin/python -m venv .venv
    fi
    source .venv/bin/activate
    echo "Nix development shell loaded."
  '';
}
