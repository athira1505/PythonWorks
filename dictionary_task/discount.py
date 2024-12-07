

fruits={"apple":45,"orange":70,"grape":800,"banana":30}

discount={k:v-v*0.1 for k,v in fruits.items()}
print(discount)