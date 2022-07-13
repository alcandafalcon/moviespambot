#removes random lines 
# didn't include it in spambot cos just need to do once before you use and I'd rather just get the file right from the get go. 
# but you probably could include it if I keep adding scripts or random crap that needs cleaning 

fh = open("beemovie.txt", "r")

with fh as infile, open('beemovienew.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line) 

