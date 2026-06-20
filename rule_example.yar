rule Detect_Suspicious_String
{
    meta:
        description = "Detects specific suspicious string"
        author = "Your Name"
    strings:
        $my_text_string = "malicious_payload_here"
        $my_hex_string = { 6A 40 68 00 30 00 00 }
    condition:
        $my_text_string or $my_hex_string
}
