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
	extend(arr[:], 7)
}

func randomAccess(nums []int) (randomNum int) {
	randomIndex := rand.Intn(len(nums))
	randomNum = nums[randomIndex]
	return
}

func extend(nums []int, enlarge int) []int {
	/*var res []int
	copy(res, nums)
	for i := len(nums); i < len(nums)+enlarge; i++ {
		res[i] = 0
	}*/
	res := make([]int, len(nums)+enlarge)
	copy(res, nums)
	return res

}
