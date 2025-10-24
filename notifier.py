# notifier.py
import boto3
from botocore.exceptions import ClientError

# ملاحظة: يجب تكوين منطقة AWS في بيئة الخادم
AWS_REGION = "eu-north-1" # استخدم نفس منطقة خادم EC2 الخاص بك
SENDER = "al.shams.invest@gmail.com" # استبدله ببريدك الإلكتروني الموثق

def send_maintenance_alert(recipient, asset_id, degradation_pct, roi_pct):
    """
    Sends a professional maintenance alert email using Amazon SES.
    """
    # استبدل هذا ببريد العميل الحقيقي (Nir Shadmi مثلاً)
    RECIPIENT = recipient

    # الموضوع ونص البريد الإلكتروني (HTML لمظهر احترافي)
    SUBJECT = f"Action Required: Predictive Maintenance Alert for Asset {asset_id}"
    
    BODY_HTML = f"""
    <html>
    <head></head>
    <body style="font-family: Arial, sans-serif; color: #333;">
        <h2>PREDAIOT™ Economic Decision Engine Alert</h2>
        <p>This is an automated alert from the PREDAIOT system.</p>
        <p>Our analysis has detected a significant performance degradation that requires immediate attention to prevent further value leakage.</p>
        <hr>
        <h3>Alert Details:</h3>
        <ul>
            <li><strong>Asset ID:</strong> {asset_id}</li>
            <li><strong>Detected Degradation:</strong> {degradation_pct:.2f}%</li>
            <li><strong>Action Prescribed:</strong> DISPATCH_MAINTENANCE</li>
            <li><strong>Predicted ROI of Action:</strong> {roi_pct:.2f}%</li>
        </ul>
        <p>Dispatching a maintenance crew is the most profitable action at this time.</p>
        <hr>
        <p style="font-size: 0.8em; color: #888;">
            This email was generated automatically by PREDAIOT™.
        </p>
    </body>
    </html>
    """

    CHARSET = "UTF-8"
    client = boto3.client('ses', region_name=AWS_REGION)

    try:
        response = client.send_email(
            Destination={'ToAddresses': [RECIPIENT]},
            Message={
                'Body': {'Html': {'Charset': CHARSET, 'Data': BODY_HTML}},
                'Subject': {'Charset': CHARSET, 'Data': SUBJECT},
            },
            Source=SENDER,
        )
    except ClientError as e:
        print(f"[ERROR] Email could not be sent: {e.response['Error']['Message']}")
        return False
    else:
        print(f"[EMAIL] Maintenance alert sent successfully to {RECIPIENT}! Message ID: {response['MessageId']}")
        return True

