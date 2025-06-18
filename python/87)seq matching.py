#write a function_matches(query:str,db:dict)
# ->list that #takes a query dna string and a dictionary of asequence IDs and sequences.
#  #returns a list of sequence IDS where the query is found as a substring. 
def find_matches(query,db,list): 
    match=[seq_id for seq_id,seq in db.items() if query in seq] 
    return match
db = { "seq001": "ATGCGGAATT",
"seq002": "CGTACGTAGC", 
"seq003": "TTATGCATTA", 
"seq004": "GGAATCCGTA",
"seq005": "CATGCCGTAGC", 
"seq006": "GGGCGTGCAT", 
"seq007": "AATGCTAGCTA",
"seq008": "CGCGATGCGC",
"seq009": "TATATATATA",
"seq010": "ATGCGGATGCA" }
query="ATGC"
List=[] 
match_seq=find_matches(query,db,List)
print(match_seq)
def generate_report(dna,db):
     count_g=0 
     count_c=0 
     if dna in db: 
        ID=db[dna] 
        for i in dna: 
            count_g=dna.count(i) 
            count_c=dna.count(i)