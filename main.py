import heapq
import networkx as nx


def dijkstra_between_works(graph, start_work):
    distances = {work: float('infinity') for work in graph}
    distances[start_work] = 0

    priority_queue = [(0, start_work)]

    while priority_queue:
        current_distance, current_work = heapq.heappop(priority_queue)

        if current_distance > distances[current_work]:
            continue

        if current_work in graph:
            for neighbor_work, weight in graph[current_work].items():
                distance = current_distance + weight

                if distance < distances[neighbor_work]:
                    distances[neighbor_work] = distance
                    heapq.heappush(priority_queue, (distance, neighbor_work))

    return distances


# 작품 간의 거리 계산 함수 (예시에서는 간단한 유클리드 거리 사용)
def calculate_distance(location1, location2):
    return ((location1[0] - location2[0]) ** 2 + (location1[1] - location2[1]) ** 2) ** 0.5


# 작가 데뷔 데이터
debut_data = {
    '김아야': 2018,
    '신교명': 2016,
    '강수빈': 2020,
    '김상희': 2017,
    '이혜주': 2012,
    '류민수': 2021,
    '안민옥&김강산': 2023,
    '김은준': 2023
}

# 위치 데이터 (가상의 예시)
location_data = {
    '작품1': (37.517838, 126.957992),
    '작품2': (37.517861, 126.958000),
    '작품3': (37.157833, 126.958070),
    '작품4': (37.517795, 126.957955),
    '작품5': (37.517895, 126.957838),
    '작품6': (37.517853, 126.957992),
    '작품7': (37.517712, 126.957588),
    '작품8': (37.517708, 126.957467),
    '작품9': (37.517730, 126.957505),
    '작품10': (37.517670, 126.957512),
    '작품11': (37.517708, 126.957497),
    '작품12': (37.517708, 126.957542),
    '작품13': (37.517708, 126.957537),
    '작품14': (37.517703, 126.957537),
    '작품15': (37.517722, 126.957528),
    '작품16': (37.517703, 126.957497),
    '작품17': (37.517703, 126.957505),
    '작품18': (37.517717, 126.957488),
    '작품19': (37.517703, 126.957450),
    '작품20': (37.517708, 126.957458),
    '작품21': (37.517720, 126.957475),
    '작품22': (37.517662, 126.957542),
    '작품23': (37.517687, 126.957505),
    '작품24': (37.517697, 126.957520),
    '작품25': (37.517697, 126.957450),
    '작품26': (37.517708, 126.957450),
    '작품27': (37.517880, 126.957947),
    '작품28': (37.517820, 126.958145),
    '작품29': (37.517820, 126.958145),
    '작품30': (37.517800, 126.958130),
    '작품31': (37.517790, 126.958120),
    '작품32': (37.517708, 126.967475)
}

# 작품과 작품 간의 관계 데이터 (가상의 예시)
works_data = {
    '김아야': ['작품1', '작품2', '작품3', '작품4', '작품5', '작품6'],
    '신교명': ['작품7', '작품8', '작품9', '작품10'],
    '강수빈': ['작품11', '작품12', '작품13', '작품14', '작품15'],
    '김상희': ['작품16', '작품17', '작품18', '작품19', '작품20', '작품21'],
    '이혜주': ['작품22', '작품23', '작품24', '작품25', '작품26'],
    '류민수': ['작품27'],
    '안민옥&김강산': ['작품28', '작품29', '작품30', '작품31'],
    '김은준': ['작품32']
}

# 그래프 생성
graph = {}
for author, works in works_data.items():
    graph[author] = {}
    for work1 in works:
        location_work1 = location_data.get(work1, (0, 0))
        for work2 in works:
            if work1 != work2:
                location_work2 = location_data.get(work2, (0, 0))
                weight = calculate_distance(location_work1, location_work2)
                graph[author][work1] = graph[author].get(work1, {})
                graph[author][work1][work2] = weight

# 작가의 최근 데뷔 순으로 정렬
sorted_authors = sorted(debut_data.keys(), key=lambda x: debut_data.get(x, 0), reverse=True)

# 다익스트라 알고리즘 호출 및 결과 출력
for author in sorted_authors:
    start_work = works_data[author][0]  # 각 작가의 첫 작품을 시작 노드로 설정
    shortest_distances = dijkstra_between_works(graph[author], start_work)

    # 최단 경로 출력
    print(f"{author}의 작품 전체를 최단 경로로 순회:")
    for work, distance in shortest_distances.items():
        print(f"{start_work}에서 {work}까지의 최단 거리: {distance}")
    print()