﻿# 🕒 PyQt5 Digital Clock
Digital Clock Image: 
![image](https://github.com/user-attachments/assets/527a8729-4407-4f18-971b-dfa7f31a67a3)


A sleek digital clock with:
- Real-time 1-second updates
- Custom DS-DIGIT.TTF font
- AM/PM time display
- Black background with green text

## Technical Highlights
```python
self.timer.start(1000)  # 1-second updates
QTime.currentTime().toString("hh:mm:ss AP")  # AM/PM formatting
QFontDatabase.addApplicationFont("DS-DIGIT.TTF")  # Custom font














