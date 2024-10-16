package test

import "core:fmt"
print :: fmt.println


main :: proc() {

	print(is_pronic(6))
	print(is_pronic(7))

}

is_pronic :: proc(n: int) -> bool {
	for i in 0 ..< n {
		if i * (i + 1) == n do return true
	}

	return false
}
