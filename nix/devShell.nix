{ pkgs }:

let
  python = pkgs.python311;
in
pkgs.mkShell {
  packages = [
    (python.withPackages
      (ps: with ps;
      [
        virtualenv # Virtualenv
        pip # The pip installer
        telethon
        numpy
        pandas
      ])
    )
  ];

}
