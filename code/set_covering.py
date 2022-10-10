def greedy_set_cover(universe, subsets, costs):
    elements = set(e for s in subsets.keys() for e in subsets[s])
    # elements don't cover universe -> invalid input for set cover
    if elements != universe:
        return None

    # track elements of universe covered
    covered = set()
    cover_sets = []

    while covered != universe:
        min_cost_elem_ratio = float("inf")
        min_set = None
        # find set with minimum cost:elements_added ratio
        for s, elements in subsets.items():
            new_elements = len(elements - covered)
            # set may have same elements as already covered -> new_elements = 0
            # check to avoid division by 0 error
            if new_elements != 0:
                cost_elem_ratio = costs[s] / new_elements
                if cost_elem_ratio < min_cost_elem_ratio:
                    min_cost_elem_ratio = cost_elem_ratio
                    min_set = s
        cover_sets.append(min_set)
        # union
        covered |= subsets[min_set]
    return cover_sets


if __name__ == '__main__':
    # universe = {1, 2, 3, 4, 5}
    # subsets = {'S1': {4, 1, 3}, 'S2': {2, 5}, 'S3': {1, 4, 3, 2}}

    # demand = {'1': 3, '2': 2, '3': 10, '4': 9, '5': 6}
  
    # def get_total_costs(subset):
    #   result = 0
    #   for s in subsets[subset]:
    #     result += demand[str(s)]

    #   return result

    # costs = {'S1': get_total_costs('S1'), 'S2': get_total_costs('S2'), 'S3': get_total_costs('S3')}
    # costs_recip = {'S1': 1/get_total_costs('S1'), 'S2': 1/get_total_costs('S2'), 'S3': 1/get_total_costs('S3')}

    # optimal_cover = optimal_set_cover(universe, subsets, costs_recip)
    # optimal_cost = sum(costs[s] for s in optimal_cover)

    # greedy_cover = greedy_set_cover(universe, subsets, costs_recip)
    # greedy_cost = sum(costs[s] for s in greedy_cover)

    # print('Optimal Set Cover:')
    # print(optimal_cover)
    # print('Cost = %s' % optimal_cost)
    # print('---------')
    # print('Greedy Set Cover:')
    # print(greedy_cover)
    # print('Cost = %s' % greedy_cost)
    
    universe = {1, 2, 3, 4, 5, 6, 7}
    subsets = {'s1': {2, 3, 4, 5}, 's2': {1, 2, 4, 5, 6}, 's3': {1, 6, 7}, 's4': { 4, 5, 6}}
    demands = {'1': 3, '2': 2, '3': 10, '4': 9, '5': 6, '6': 11, '7': 4}
    
    def get_costs(subsets):
      costs = {}
      for subset, elements in subsets.items():
        cost = 0
        for e in elements:
          cost += demands[str(e)]
        
        costs[subset] = cost
        
      costs_recip = {}
      
      for k, v in costs.items():
        costs_recip[k] = 1/v
        
      return [costs, costs_recip]
    
    costs, costs_recip = get_costs(subsets)
    
    greedy_cover = greedy_set_cover(universe, subsets, costs_recip)
    greedy_cost = sum(costs[s] for s in greedy_cover)
    print(greedy_cover)
    print(greedy_cost)
    

#! cost를 무엇으로 하나? 
# 수요가 최대가 되도록 cover를 구한다? 
# 1. 음수로 취하면 모든 점을 다 찍어버림
# 2. 역수로 취하면 얼핏 나옴. 하지만 greedy한 알고리즘이기 때문에 최적해는 되지 못함.(optimal을 사용하면 최적해를 구하지만 시간 복잡도가 너무 크기 때문에 실제 데이터에는 적용 불가능)

#! subset의 엘리먼트 커버 기준? 일정 거리 내에 존재하는 cell.
# 약 1000개의 후보지 X 12000개의 cell 갯수
# subset의 coverage를 구하는데도 시간이 좀 걸릴듯?