def tokenize( program ):
	return program.replace('<',' < ').replace('>',' > ').split()
