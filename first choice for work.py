tecrube_ili= float(input("Tecrube ilini daxil edin: "))
texiniki_musahibe_bali= float(input("Texiniki musahibe balini daxil edin (0-100): "))
if tecrube_ili >= 2 and texniki_musahibe_bali >=70:   
elif (texniki_musahibe_bali >= 90):
result = "Novbeti merheleye devet olundu." if "Guclu namized" else "Namized uygun deyil."
xeta = "Xeta: Menfi tecrube ve ya 0-100 araliginda kenar bal daxil edile bilmez!" if tecrube_ili < 0 or texniki_musahibe_bali < 0 or texniki_musahibe_bali > 100 else None
print(result, xeta)







