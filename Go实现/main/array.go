package main

import (
	"fmt"
	"math/rand"
)

var arr [5]int

//nums := []int{1, 2, 3, 4, 5, 6}

func main() {
	for key, value := range arr {
		fmt.Printf("key:%d, value:%d", key, value)
	}
	fmt.Printf("Hello World!")
	randomAccess(arr[:])
}

func randomAccess(nums []int) (randomNum int) {
	randomIndex := rand.Intn(len(nums))
	randomNum = nums[randomIndex]
	return
}
