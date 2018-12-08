#!/usr/bin/env bash

function getMachineType {
  unameOut="$(uname -s)"
  case "${unameOut}" in
      Linux*)     machine=Linux;;
      Darwin*)    machine=Mac;;
      CYGWIN*)    machine=Cygwin;;
      MINGW*)     machine=MinGw;;
      *)          machine="UNKNOWN:${unameOut}"
  esac
  echo ${machine}
}

checkIfCmdExists () {
    command -v "$1" >/dev/null
}

machine=$(getMachineType)
if ! command -v python3 &>/dev/null
then
  if ${machine} == "Mac"
  then
      if ! $(checkIfCmdExists brew)
      then
        echo "Installing python with brew"
        brew install python3
      else
        echo "This script requires homebrew"
      fi
  elif ${machine} == "Linux"
  then
      if ! $(checkIfCmdExists apt-get)
      then
        echo "Updating apt-get"
        apt-get update
        echo "Installing python 3 with apt-get"
        apt-get install python3.7
      fi
  fi
else
  echo "Python3 is installed"
fi

if ! command -v pip &>/dev/null
then
  echo 'pip is not installed'
  easy_install pip
else
  echo "pip is already installed"
fi

if [[ $* == *-o* ]] || ! $(checkIfCmdExists aztest)
then
  pip install --editable .
  echo "Installed aztest cli"
else
  echo "The cli is already installed. Skipping installation. If you want to override add the override flag [-o]."
  echo "Example: ./install_cli.sh -o"
fi

echo "Run aztest --help for details"
