# Desktop build
gcc *.c -lraylib -lGL -lm -lpthread -ldl -lrt -lX11 -L . -o game


# Web build 
### drop # the web version of raylib.a 
~~emcc -o game.html main.c -Os -Wall libraylib.a -I. -L. -s USE_GLFW=3 -s ASYNCIFY --shell-file shell.html -DPLATFORM_WEB --preload-file resources~~
em++ -o game.html $1 -Os -Wall libraylib.a -I. -L. -s USE_GLFW=3 -s ASYNCIFY --shell-file minshell.html -DPLATFORM_WEB --preload-file resources -s ALLOW_MEMORY_GROWTH=1
