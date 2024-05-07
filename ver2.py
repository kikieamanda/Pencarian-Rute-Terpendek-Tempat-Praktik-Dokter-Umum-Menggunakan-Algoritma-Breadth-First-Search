import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Graph:
    def __init__(self):
        self.G = nx.Graph()
        self.codes = []
        self.names = []

    def add_node(self, code, name, latitude, longitude):
        self.G.add_node(code, name=name, latitude=latitude, longitude=longitude)
        self.codes.append(code)
        self.names.append(name)

    def add_edge(self, node1, node2, weight=0):
        self.G.add_edge(node1, node2, weight=weight)
        
    def create_graph(self):
        # Menambahkan node 
        nodes = [("D1", "Dr. Abdul ", -7.33416651, 112.81106319),
                 ("D2", "Dr. Fitri Yuda Mayasari", -7.34177390, 112.80172376),
                 ("D3", "Dr. Ani Budiwati", -7.33597052, 112.80002715),
                 ("D4", "Dr. Eko Iswahyudi", -7.33652257, 112.79632167),
                 ("D5", "Dr. Jimmy S.", -7.33331395, 112.79686486),
                 ("D6", "Dr. Luksadi", -7.33149401, 112.77200001),
                 ("D7", "Dr. Brana Pradata", -7.33603313, 112.76843121),
                 ("T1", "Mushola & TPQ Jl. Wisma Tirta Agung Asri", -7.33716645, 112.81448358),
                 ("T2", "Perumahan Wisma Indah", -7.33607377, 112.81059970),
                 ("T3", "Musholla AlFattah Puri Gununganyar Regency", -7.33533380, 112.81152717),
                 ("T4", "Taman Gunung Anyar", -7.33464206, 112.80900963),
                 ("T5", "Rusunawa Gunung Anyar", -7.33095389, 112.81475987),
                 ("T6", "Musholla Hubbul Wathon", -7.33199479, 112.80540012),
                 ("T7", "Masjid Al Muttaqin, Gunung Anyar Emas", -7.33440798, 112.80317085),
                 ("T8", "Bengkel cat mobil Grand Star", -7.33271733, 112.80077577),
                 ("T9", "DAMKAR GUNUNG ANYAR", -7.33805311, 112.80194598),
                 ("T10", "Masjid Nur Madrikah", -7.33838505, 112.80006815),
                 ("T11", "Panti Asuhan Ulul Azmi", -7.34039890, 112.80190324),
                 ("T12", "SD Budi Mulia Islamic Shool", -7.34269705, 112.80575107),
                 ("T13", "Gunung Anyar Town House", -7.34425333, 112.80543159),
                 ("T14", "Masjid Roudlotul Mukminin", -7.34414147, 112.80155038),
                 ("T15", "Gunung Anyar Asri", -7.34375594, 112.80123834),
                 ("T16", "PERUM BUMI PRATAMA ASRI", -7.34337962, 112.80019323),
                 ("T17", "Politeknik Pelayaran Surabaya", -7.34302591, 112.79479166),
                 ("T18", "Perumahan Gunung Anyar Permai", -7.33860742, 112.79596451),
                 ("T19", "Masjid al Mubarok", -7.33669157, 112.79508927),
                 ("T20", "PT. Berhasil Sinar Gemilang Abadi", -7.33390413, 112.79720483),
                 ("T21", "Apotek Doa Sehat", -7.33470896, 112.79576748),
                 ("T22", "SPBU Pertamina - Gunung Anyar", -7.33344254, 112.79394668),
                 ("T23", "Fotocopy Alfin", -7.33294780, 112.79221827),
                 ("T24", "UPN 'Veteran' Jawa Timur", -7.33225209, 112.78849596),
                 ("T25", "Mr. Suprek Rungkut", -7.33157163, 112.78298514),
                 ("T26", "Masjid Assalam Purimas", -7.33903455, 112.78466655),
                 ("T27", "UINSA Kampus 2", -7.34422439, 112.78665880),
                 ("T28", "McDonald's - Rungkut Madya", -7.33132323, 112.77560415),
                 ("T29", "SPBU Pertamina 54.601.99 Rungkut Mapan", -7.33477780, 112.77505521),
                 ("T30", "SDN Rungkut Mananggal I", -7.33605799, 112.77330609),
                 ("T31", "Masjid Al-Muslimun", -7.33668695, 112.77288917),
                 ("T32", "Kantor Kelurahan Rungkut Tengah", -7.33312868, 112.77110175),
                 ("T33", "Masjid At-Taibin", -7.33302809, 112.76853020),
                 ("T34", "Kantor Kelurahan Rungkut Mananggal", -7.33746547, 112.76860250),
                 ("T35", "Pondok Pesantren Manbaul Falah", -7.33895626, 112.76793831),
                 ("T36", "Taman Rungkut Mananggal", -7.33850203, 112.76706837),
                 ("T37", "Masjid Baiturrozaq SIER Surabaya", -7.33222082, 112.75701217)]

        for node in nodes:
            code, name, latitude, longitude = node
            self.add_node(code, name, latitude, longitude)
        
        # Menambahkan edge 
        edges = [("T1", "T2", 0.51),
                 ("T1", "T3", 0.54),
                 ("T2", "T4", 0.35),
                 ("T3", "T4", 0.36),
                 ("T3", "D1", 0.15),
                 ("T4", "D1", 0.28),
                 ("T5", "D1", 0.91),
                 ("T4", "T6", 0.66),
                 ("T5", "T6", 1.04),
                 ("T6", "T7", 0.42),
                 ("T6", "T8", 0.53),
                 ("T8", "D3", 0.44),
                 ("T9", "D3", 0.59),
                 ("T10", "D3", 0.27),
                 ("T9", "T11", 0.26),
                 ("T11", "D2", 0.15),
                 ("T12", "D2", 0.54),
                 ("T12", "T13", 0.18),
                 ("T13", "T14", 0.56),
                 ("T14", "D2", 0.77),
                 ("T14", "T15", 0.64),
                 ("T15", "T16", 0.14),
                 ("T16", "T17", 0.64),
                 ("T17", "T18", 0.56),
                 ("T18", "T11", 0.7),
                 ("T14", "T27", 2.27),
                 ("T18", "T19", 0.36),
                 ("T19", "D4", 0.14),
                 ("D3", "D4", 0.54),
                 ("T8", "D5", 0.43),
                 ("T20", "D5", 0.13),
                 ("T19", "T21", 0.26),
                 ("T21", "T22", 0.35),
                 ("T22", "D5", 0.32),
                 ("T22", "T23", 0.24),
                 ("T23", "T24", 0.47),
                 ("T24", "T25", 0.61),
                 ("T24", "T26", 1.08),
                 ("T25", "T26", 1.15),
                 ("T25", "T28", 0.81),
                 ("T26", "T27", 0.83),
                 ("T26", "T28", 1.56),
                 ("T28", "T29", 0.42),
                 ("T29", "T30", 0.43),
                 ("T30", "T31", 0.2),
                 ("T28", "D6", 0.42),
                 ("T32", "D6", 0.26),
                 ("T33", "D6", 0.53),
                 ("T33", "D7", 0.33),
                 ("T34", "D7", 0.17),
                 ("T34", "T35", 0.22),
                 ("T35", "T36", 0.1),
                 ("T37", "D6", 1.88)]

        for edge in edges:
            node1, node2, weight = edge
            self.add_edge(node1, node2, weight)   
            
    def get_nodes_codes(self):
        return self.codes
        
    def get_nodes_names(self):
        return self.names
    
    
    def show_graph(self):
        pos = {node: (data['longitude'], data['latitude']) for node, data in self.G.nodes(data=True)}
        labels = {node: node for node in self.G.nodes()}
        edge_labels = {(u, v): f"{weight:.2f}" for u, v, weight in self.G.edges(data='weight')}
        
        plt.figure(figsize=(15,10))
        nx.draw_networkx(self.G, pos=pos, with_labels=False, node_size=200, node_color='skyblue')
        nx.draw_networkx_labels(self.G, pos=pos, labels=labels, font_size=8, font_color='black')
        nx.draw_networkx_edge_labels(self.G, pos=pos, edge_labels=edge_labels, font_size=8)
        plt.axis('off')
        plt.show()

class bfs:
    def __init__(self, graph):
        self.G = graph.G
        
    def shortest_path(self, start_node):
        try:
            if start_node not in self.G.nodes:
                raise ValueError("Invalid start node")

            queue = deque()
            visited = set()
            distance = {}
            parents = {}

            queue.append(start_node)
            visited.add(start_node)
            distance[start_node] = 0
            parents[start_node] = None

            while queue:
                current_node = queue.popleft()

                if current_node[0] == 'D':
                    # Jika simpul dengan indeks pertama "D" ditemukan, dokter terdekat ditemukan
                    path = []
                    parent = parents[current_node]
                    path.append(current_node)
                    while parent:
                        path.append(parent)
                        parent = parents[parent]
                    path.reverse()
                    distance = distance[current_node]
                    return path, distance

                for neighbor in self.G[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        distance[neighbor] = distance[current_node] + self.G.edges[current_node, neighbor]["weight"]
                        parents[neighbor] = current_node

            # Jika dokter tidak ditemukan, kembalikan None
            return "Dokter terdekat tidak ditemukan"
        except ValueError as e:
            print(str(e))

    def print_result(self, start_node, path, distance):
            if path:
                print("Jalur terdekat:", " -> ".join(path))
                print(f"Jarak terdekat dari {start_node} ke dokter terdekat: {distance:.2f} km")
            else:
                print("Tidak ada dokter yang ditemukan")