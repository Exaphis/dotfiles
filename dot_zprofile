case `uname` in
Darwin)
    eval $(/opt/homebrew/bin/brew shellenv)
    eval "$(pyenv init --path)"

    # >>> JVM installed by coursier >>>
    export JAVA_HOME="/Users/kevin/Library/Caches/Coursier/arc/https/github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u292-b10/OpenJDK8U-jdk_x64_mac_hotspot_8u292b10.tar.gz/jdk8u292-b10/Contents/Home"
    # <<< JVM installed by coursier <<<

    # >>> coursier install directory >>>
    export PATH="$PATH:/Users/kevin/Library/Application Support/Coursier/bin"
    # <<< coursier install directory <<<
    ;;
Linux)
    ;;
esac

# purdue server specific settings
if hostname | grep purdue.edu > /dev/null; then
    # set TERM variable to avoid terminal is not fully functional warnings
    export TERM='xterm-256color'

    # strip permissions from group and others
    umask 077

    # CS354 Xinu lab setup
    export PATH=${PATH}:/p/xinu/bin
    export CS_CLASS=cortex
fi

