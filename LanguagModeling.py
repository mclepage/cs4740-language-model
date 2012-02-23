import pickle, pprint, json

#file_path = raw_input("File path to text file: ")
#pickle_path = raw_input("File path for pickled output: ")



def generate_unigram(file_path):
	f = open(file_path)
	words = f.read().split()
	word_count = len(words)
	unigrams = {}
	for i in range(word_count):
		word=words[i]
		if word not in unigrams:
			unigrams[word]=1.0
		else:
			unigrams[word]=unigrams[word]+1
	for word in unigrams:
		unigrams[word] = float(unigrams[word])/word_count
	return unigrams

	
	
def generate_bigrams(file_path):
	f = open(file_path)
	bigrams={}
	words = f.read().split()
	for i in range(len(words)-1):
		word=words[i]
		if word not in bigrams:
			bigrams[word]={}
		second_word = words[i+1]
		if second_word not in bigrams[word]:
			bigrams[word][second_word] = 1
		else:
			bigrams[word][second_word] = bigrams[word][second_word]+1
	for word in bigrams:
		count = 0.0
		for second_word in bigrams[word]:
			count += bigrams[word][second_word]
		for second_word in bigrams[word]:
			bigrams[word][second_word] = float(bigrams[word][second_word])/count
	return bigrams


def generate_ngrams(file_path, n):
	f = open(file_path)
	ngrams={}
	start_level = [{}, 0.0, 0.0]
	words = f.read().split()
	for i in range(len(words)+1):
		subset = words[i:i+n]
		cur_dict=ngrams
		cur_level = start_level
		#if "__count" not in cur_dict[subset[0]]:
		#	cur_dict[subset[0]]["__count"] = 0.0
		#cur_dict[subset[0]]["__count"] = cur_dict[subset[0]]["__count"] + 1
		while subset!=[]:
			cur_word = subset[0]
			subset=subset[1:]
			if cur_word not in cur_dict:
				cur_dict[cur_word]={"__count":0.0, "__freq":0.0}
			if cur_word not in cur_level[0]:
				next_level = [{}, 0.0, 0.0]
				cur_level[0][cur_word] = next_level
			cur_level[0][cur_word][1] = cur_level[0][cur_word][1] + 1
			cur_level = cur_level[0][cur_word]
			cur_dict=cur_dict[cur_word]
			cur_dict["__count"] = cur_dict["__count"]+1
	cur_dict = ngrams
	cur_level = start_level
	print cur_level
	for i in range(n):
		sum_counts = float(sum(cur_level[0][key][1] for key in cur_level[0]))
		for key in cur_level[0]:
			cur_level[0][key][2] = cur_level[0][key][1]/sum_counts
		sum_counts = float(sum(cur_dict[key]["__count"] for key in cur_dict))
		for key in cur_dict:
			cur_dict[key]["__freq"] = cur_dict[key]["__count"]/sum_counts
	return ngrams
	return start_level
		

def generate_ngramsCLEAN(file_path, n):
	f = open(file_path)
	start_level = [{}, 0.0, 0.0]
	words = f.read().split()
	for i in range(len(words)+1):
		subset = words[i:i+n]
		cur_level = start_level
		while subset!=[]:
			cur_word = subset[0]
			subset=subset[1:]
			if cur_word not in cur_level[0]:
				next_level = [{}, 0.0, 0.0]
				cur_level[0][cur_word] = next_level
			cur_level[0][cur_word][1] = cur_level[0][cur_word][1] + 1
			cur_level = cur_level[0][cur_word]
	cur_level = start_level
	print cur_level
	for i in range(n+1):
		sum_counts = float(sum(cur_level[0][key][1] for key in cur_level[0]))
		for key in cur_level[0]:
			cur_level[0][key][2] = cur_level[0][key][1]/sum_counts
	return start_level


n =  generate_ngrams("EnronDataset/simpletext.txt", 3)
print n
print(json.dumps(n, indent=4))




#for key in n:
#	print key+" : "
#	for key2 in n[key]:
#		print "  "+key2+"  " +str(n[key][key2])
		