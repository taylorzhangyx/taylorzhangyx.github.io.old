package main

import (
	"crypto/md5"
	"fmt"
	"sort"
	"strings"
)

type T struct {
	Dims []struct{
		K string
		V string
	}
	AppID string
	IssueUUID string
}

const ss = "\t\"SubIssue-0d8bed2efe#D99569F467CE39019DA30B31D8FF07B3#ProdVer:6578-7958305180CCA780707FA3B99019C679\"\n"

var sd = T {
	Dims: []struct{
		K string
		V string
	}{
		{
			K:"ProdVer",
			V:"6578",
		}},
	AppID:     "0d8bed2efe",
	IssueUUID: "D99569F467CE39019DA30B31D8FF07B3",
}

func main()  {
	fmt.Println("fdaewf")


	// 前缀拼接issueUUID，以优化 issue 维度的查询效率
	var dimstrs []string
	for _, d := range sd.Dims {
		dstr := fmt.Sprintf("%v:%v", d.K, d.V)
		dimstrs = append(dimstrs, dstr)
	}
	sort.Strings(dimstrs)
	hash := md5.Sum([]byte(fmt.Sprintf("%v#%v", sd.AppID, strings.Join(dimstrs, "#"))))

	s := fmt.Sprintf("%v%X", sd.IssueUUID, hash[:8])
	fmt.Println(s)
}