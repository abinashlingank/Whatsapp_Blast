# Whatsapp_Blast
Automated message sender with attachments

# bulk_messager_for_whatsapp_with_attachment

Bulk Messager for whatsapp is a python code that automates sending of messages via Whatsapp Web with attachment. The tool can you used to send whatsapp message with an attachment in bulk. Program uses runs through a list of numbers provided in numbers.txt and then tries to send a prediefined message to each number in the list.

Note: This Program can be used send text message with one attachment

# Requirements

*  Python >= 3.6
*  Chrome headless which can be installed by the program automatically

# Setup

1. Install python - >=v3.6
2. Create one virtual environment named "whatsapp" by run the command `python -m venv whatsapp`
3. Run `cd whatsapp/scripts`
4. Run `activate.bat`
5. Run `cd ../..`
6. Run `pip install -r requirements.txt`

# Steps

1. Enter the message you want to send inside `message.txt` file.
2. Enter the list of numbers line-separated in `numbers.txt` file.
3. Specify the attachment path in the `main.py line no 70`
4. Run `python main.py`.
5. **Note for Talos students: use main2.py for Image Caption messages(Put your messages in `message1.txt` and `message2.txt`)
6. Once the program starts, you'll see the message in message.txt and count of numbers in the numbers.txt file.
7. After a while, Chrome should pop-up and open web.whatsapp.com.
8. Scan the QR code to login into whatsapp.
9. Press `Enter` to start sending out messages.
10. Sit back and relax!
