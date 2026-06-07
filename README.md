# 🛒 Django E-Ticaret Projesi (Full Stack)

Bu proje, Django framework kullanılarak geliştirilmiş kapsamlı bir e-ticaret sistemidir. Ürün yönetimi, varyant sistemi, sepet, sipariş, kullanıcı yönetimi ve yorum sistemi gibi modern bir e-ticaret platformunda bulunması gereken tüm temel bileşenleri içerir.

---

## 🚀 Proje Özeti

Kullanıcılar:
- Ürünleri kategori bazlı inceleyebilir
- Varyant seçebilir (renk, beden vb.)
- Sepete ürün ekleyebilir
- Sipariş oluşturabilir
- Yorum yapabilir ve puan verebilir
- Profil bilgilerini güncelleyebilir

Admin:
- Ürün & kategori yönetimi
- Varyant & attribute yönetimi
- Sipariş takibi
- Yorum moderasyonu
- Stok kontrolü

---

## 🧱 Kullanılan Teknolojiler

- Python 3
- Django Framework
- SQLite / PostgreSQL
- HTML5, CSS3
- Bootstrap 5
- JavaScript (AJAX)
- Django MPTT (kategori ağacı)
- Django Messages Framework
- Django Auth System
- CKEditor

---

## 📦 Uygulama Modülleri

### 🛍 Product App
- Ürün yönetimi
- Kategori (tree structure)
- Varyant sistemi
- Attribute & AttributeValue
- Ürün görselleri
- Yorum sistemi

### 🛒 Order App
- Sepet sistemi
- Sipariş oluşturma
- Order / OrderProduct modeli
- Stok düşme mekanizması

### 👤 Users App
- Login / Register
- UserProfile yönetimi
- Profil güncelleme
- Şifre değiştirme

---

## 🔥 Öne Çıkan Özellikler

### 📌 Varyant Sistemi
- Her ürün için birden fazla varyant
- Slug bazlı routing
- Attribute tabanlı seçim (renk, beden vb.)

### 🛒 Sepet Sistemi
- Kullanıcı bazlı sepet
- Quantity update sistemi
- Stok kontrolü

### 📦 Sipariş Sistemi
- Sipariş kodu üretimi
- OrderProduct detay yapısı
- Sipariş sonrası stok düşme

### 💬 Yorum Sistemi
- AJAX yorum gönderimi
- Rating sistemi (1-5)
- Sadece login kullanıcılar

### 👤 Profil Sistemi
- Kullanıcı bilgileri
- Profil resmi
- Dil & currency desteği

---

## 🗂 Veritabanı Yapısı

- Product
- Category (MPTT)
- Variants
- Attribute / AttributeValue
- ShopCart
- Order / OrderProduct
- Comment
- UserProfile

---

## 🔐 Authentication

- Django built-in auth
- Session-based login
- Signup / Login / Logout
- Password change

---
