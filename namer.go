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
*/

//go:embed english.txt
var DICTIONARY string
var DICTIONARY_WORDS []string
var DIC_LEN int


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

    if len(os.Args) > 1 && os.Args[1] == "-h" {
        fmt.Println("run with namer (options word_count, max_word_length, will default to 4 and 6)")
        os.Exit(0)
    }

    fmt.Println(os.Args) 

    COUNT := 4  // default
    LENGTH := 6 // default
    if len(os.Args) == 3 {
        COUNT, _ = strconv.Atoi(os.Args[1])
        LENGTH, _ = strconv.Atoi(os.Args[2])
    }

    r := gen_random()
    gen_name := generate_name(COUNT, LENGTH, r) 
    fmt.Println(gen_name)
}
