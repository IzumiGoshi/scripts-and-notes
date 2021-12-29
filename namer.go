package main

import (
    _ "embed"
    "fmt"
    "math/rand"
    "os"
    "strconv"
    "strings"
    "time"
)

/*
   this is a small script to generate a unique
   filename by stringing together words from the
   linux words file.

   ex
   namer ~/Pictures jpg
   will generate a file like this
   /home/IzumiGoshi/Pictures/GwynAugerKentonAngers.jpg

   the default is to use 4 words
   that are at max 6 characters long.

   this can also be set 
   namer ~/Pictures jpg 3 3
   /home/IzumiGoshi/Pictures/MayZedPin.jpg

*/

//go:embed english.txt
var DICTIONARY string
var DICTIONARY_WORDS []string
var DIC_LEN int

// returns (name, extension)
func extension(fname string) (string, string) {
    split := strings.Split(fname, ".")
    namespl := split[:len(split)-1]
    name := strings.Join(namespl, ".")
    ext := split[len(split)-1]
    return name, ext
}

func gen_random() *rand.Rand {
    s1 := rand.NewSource(time.Now().UnixNano())
    r1 := rand.New(s1)
    return r1
}

func format_word(word string) string {
    word = strings.Replace(word, "'", "", -1)
    word = strings.Title(word)
    return word
}

func generate_name(word_count int, length int, r *rand.Rand) string {
    var words []string
    rand_word_index := 0
    next_word := ""

    for {
        rand_word_index = r.Intn(DIC_LEN)
        next_word = DICTIONARY_WORDS[rand_word_index]

        if len(next_word) <= length {
            next_word = format_word(next_word)
            words = append(words, next_word)
        }

        if len(words) == word_count {
            break
        }
    }
    return strings.Join(words, "")
}

func main() {
    DICTIONARY_WORDS = strings.Split(DICTIONARY, "\n")
    DIC_LEN = len(DICTIONARY_WORDS)

    if os.Args[1] == "-h" {
        fmt.Println("namer   /my/dir   file_extension   word_count   max_word_length")
        os.Exit(0)
    }

    DIR := os.Args[1]
    FILE_EXTENSION := os.Args[2]

    COUNT := 4  // default
    LENGTH := 6 // default
    if len(os.Args) == 5 {
        COUNT, _ = strconv.Atoi(os.Args[3])
        LENGTH, _ = strconv.Atoi(os.Args[4])
    }

    r := gen_random()
    gen_name := ""
    new_file := ""

    for {
        gen_name = generate_name(COUNT, LENGTH, r)
        new_file = DIR + "/" + gen_name + "." + FILE_EXTENSION
        if _, err := os.Stat(new_file); os.IsNotExist(err) {
            break
        }
    }
    fmt.Println(new_file)
}
