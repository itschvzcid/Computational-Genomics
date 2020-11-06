# Función asociada al programa 01
def getPercentOff(discount, total):
	message = 'La compra es de '
	message += str(total)
	if total > 100:
		total = total - (total * (discount / 100))
		message += ', siendo >100, tuvo descuento del '
		message += str(discount)
		message += ', precio final de '
		message += str(total)
	return message

# Función asociada al programa 02
def getTriangleArea(b, h):
	area = (b * h) / 2
	#print(area)
	if area.is_integer():
		print("Base: ", b, ", Altura: ", h, ", Área triángulo: ", int(area))
	else:
		print("Base: ", b, ", Altura: ", h, ", Área triángulo: ", "{0:.2f}".format(area))

# Función asociada al programa 03
def getBMI(w, h):
	return w / (h**2)

# Main
def main():

	print(getPercentOff(10, 90))
	print(getPercentOff(10, 100))
	print(getPercentOff(10, 8793))

	getTriangleArea(5, 10)
	getTriangleArea(5.25, 10.7575)

	f03 = getBMI(80, 1.80)
	print("IMC: ", "{0:.2f}".format(f03))


if __name__ == "__main__":
	main()

