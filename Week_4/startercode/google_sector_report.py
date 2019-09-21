import json

def get_biggest_movers(filename):
    from bs4 import BeautifulSoup
    file = open(filename, "r").read()
    soup = BeautifulSoup(file, "lxml")
    empty_list = []
    for tr in soup.find_all("table", class_="topmovers"):
        for row in tr.find_all("tr"):
            for item in row.find_all("td"):
                empty_list.append(item.get_text())
    stock, increase = " ".join(empty_list[4].split()), empty_list[7].split()
    clean_increase = increase[1].strip("(%)")
    return (stock, float(clean_increase))

def get_biggest_losers(filename):
    from bs4 import BeautifulSoup
    file = open(filename, "r").read()
    soup = BeautifulSoup(file, "lxml")
    empty_list = []
    for tr in soup.find_all("table", class_="topmovers"):
        for row in tr.find_all("tr"):
            for item in row.find_all("td"):
                empty_list.append(item.get_text())
    stock, decrease = " ".join(empty_list[31].split()), empty_list[34].split()
    clean_decrease = decrease[1].strip("(%)")
    return (stock, float(clean_decrease))

def get_biggest_sectors(filename):
        from bs4 import BeautifulSoup
        file = open(filename, "r").read()
        soup = BeautifulSoup(file, "lxml")
        empty_list = []
        for tr in soup.find_all("div", class_="id-secperf sfe-section-major"):
            for row in tr.find_all("tr"):
                for item in row.find_all("td"):
                    empty_list.append(item.get_text().split())
        energy = "".join(empty_list[4])
        energy = energy.strip("%")
        basic_materials = "".join(empty_list[20])
        basic_materials = basic_materials.strip("%")
        industrials = "".join(empty_list[36])
        industrials = industrials.strip("%")
        return (energy, basic_materials, industrials)

def google_sector_report():
    energy_mover = get_biggest_movers("energy.htm")
    energy_loser = get_biggest_losers("energy.htm")
    basic_mover = get_biggest_movers("basic materials.htm")
    basic_loser = get_biggest_losers("basic materials.htm")
    indust_mover = get_biggest_movers("industrials.htm")
    indust_loser = get_biggest_losers("industrials.htm")

    energy, basic_materials, industrials = get_biggest_sectors("Google Finance.htm")
    results = {
        "result" : {
            "energy" : {
                "biggest_gainer" : {
                    "equity" : energy_mover[0],
                    "change" : energy_mover[1]
                },
                "biggest_loser" : {
                    "equity" : energy_loser[0],
                    "change" : energy_loser[1]
                },
                "change" : energy
            },
            "basic materials" : {
                "biggest_gainer" : {
                    "equity" : basic_mover[0],
                    "change" : basic_mover[1]
                },
                "biggest_loser" : {
                    "equity" : basic_loser[0],
                    "change" : basic_loser[1]
                },
                "change" : basic_materials
            },
            "Industrials" : {
                "biggest_gainer" : {
                    "equity" : indust_mover[0],
                    "change" : indust_mover[1]
                },
                "biggest_loser" : {
                    "equity" : indust_loser[0],
                    "change" : indust_loser[1]
                },
                "change" : industrials
            }
        }
    }
    json_string = json.dumps(results)
    return json_string

print(google_sector_report())
