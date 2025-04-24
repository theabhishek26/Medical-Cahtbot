import os

print("\n📁 Current Working Directory:")
print(os.getcwd())

print("\n📂 Files and folders in current directory:")
print(os.listdir("."))

if os.path.exists("templates"):
    print("\n✅ 'templates' folder found.")
    print("📄 Files in 'templates':", os.listdir("templates"))
    
    if os.path.exists("templates/chat.html"):
        print("✅ 'chat.html' exists in 'templates' folder.")
    else:
        print("❌ 'chat.html' NOT found in 'templates' folder.")
else:
    print("❌ 'templates' folder NOT found.")
