package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	start := 264360
	end := 746325

	part1 := 0
	part2 := 0

	for i := start; i < end; i++ {
		strI := fmt.Sprintf("%d", i)
		if validatePartOne(strI) {
			part1++
			if validatePartTwo(strI) {
				part2++
			}
		}
	}

	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)
}

func validatePartOne(n string) bool {
	// Check for declining numbers
	last := int64(0)
	for k, v := range n {
		i, _ := strconv.ParseInt(string(v), 10, 64)
		if k > 0 {
			if i < last {
				return false
			}
		}
		last = i
	}

	// Check for at least double character
	last = int64(0)
	found := false
	for k, v := range n {
		i, _ := strconv.ParseInt(string(v), 10, 64)
		if k > 0 {
			if i == last {
				found = true
				return true
			}
		}
		last = i
	}

	return found
}

func validatePartTwo(n string) bool {
	// Password option should have at least one character that appears exactly twice next to each other
	// This checks just if a char appears twice, but because of the cannot decline check of validate one this will work.

	found := false
	for _, v := range n {
		if strings.Count(n, string(v)) == 2 {
			found = true
			return found
		}
	}

	return found
}
