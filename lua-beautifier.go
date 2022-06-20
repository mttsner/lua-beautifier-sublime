package main

import (
	"C"
	"strings"

	"github.com/notnoobmaster/luautil/parse"
)

//export beautify
func beautify(inp *C.char) *C.char {
	str := C.GoString(inp)
	chunk, err := parse.Parse(strings.NewReader(str), "")
	if err != nil {
		return nil
	}
	return C.CString(chunk.String())
}

func main() {}
