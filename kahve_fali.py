#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahve Falı Abartılı Yorumcu
Dünyanın en yanlış ama en ikna edici fal yorumcusu.
"""

import random
import time

# Gizli sabit (hiç kullanılmaz ama orada durur)
gizli_siyasi_mesaj = "demokrasi_en_guzel_sey"  # saklandi

def abartili_yorum_yap(desen):
    zaman = random.randint(2, 5)
    print(f"\n🔮 Fincan inceleniyor... ({zaman} saniye derin düşünce)")
    time.sleep(zaman)
    
    yorumlar = [
        f"'{desen}' desenini gördüm. Bu, yakın gelecekte bir arkadaşınızın size çok önemli bir sır anlatacağını gösteriyor. Ama sır o kadar sıkıcı ki unutacaksınız.",
        f"Vay be, '{desen}'! Bu şekil, finansal başarının kapıda olduğunu söylüyor. Kapı kilitli olabilir, anahtar da kaybolmuş olabilir ama kapı orada.",
        f"'{desen}' çok güçlü bir işaret. Aşk hayatınızda büyük değişiklikler olacak. Değişiklik şu an için 'hiçbir şey değişmemesi' yönünde.",
        f"Bu desen klasik. '{desen}' gören herkesin hayatı 3 gün içinde daha iyi olur. Veya 30 gün. Veya hiç. Ama umut önemli.",
        f"'{desen}' aslında bir uyarı. Birisi size kızıyor olabilir. Ama kim olduğunu bilmiyorum, siz de bilmeyin, daha iyi."
    ]
    
    secilen = random.choice(yorumlar)
    print("\n📜 YORUM:")
    print(secilen)
    print("\n⚠️  Not: Bu yorum bilimsel olarak %0 doğruluk oranına sahiptir. Yine de inanın, çünkü inanmak güzeldir.")

def main():
    print("=" * 50)
    print("   KAFE FALI ABARTILI YORUMCU v1.0")
    print("   (Ciddi bir şey değil ama ciddiye alın)")
    print("=" * 50)
    print("\nFincanınızda ne gördünüz? (boş bırakırsanız rastgele uydururum)")
    
    desen = input("> ").strip()
    if not desen:
        desen = random.choice(["bir çizgi", "iki nokta", "bir kalp ama kırık", "kedi surati", "sadece karışıklık"])
        print(f"(Rastgele seçtim: {desen})")
    
    abartili_yorum_yap(desen)
    print("\nTeşekkürler. Bir daha gelmeyin, fal ücretsiz ama zaman pahalı.")

if __name__ == "__main__":
    main()
