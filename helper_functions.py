import smtplib, ssl
import random

### CONSTANTS ###
_DIGENERATOR_NAMES = ['Cyberly', 'cybercyan', 'cybera', 'datackr', 'retrics', 'updatas', 'tections', 'stackrally', 'infobase', 'serverse', 'techinet', 'ai-cube', 'configun', 'keybot', 'enginet', 'hexachine', 'boot-AI', 'compuengine', 'cyberwire', 'Treakserver', 'desklab', 'serverlab', 'powereye', 'infostack', 'systack', 'probot', 'tenzer', 'syscale', 'tigerscale', 'qualitynet', 'spoolix', 'xenomVR', 'blockstitch', 'pirobot', 'roboble', 'gearlytics', 'sys', 'swiftMR', 'codelbit', 'compinet', 'andromada', 'swiqy', 'kubershade', 'dockereverse']
 
_DIGENERATOR_VERBS = ["initialize", "implement", "utilize", "integrate", "streamline", "optimize", "evolve", "transform", "embrace", 
"enable", "orchestrate", "leverage", "reinvent", "aggregate", "architect", "enhance", "incentivize", "morph", "empower", 
"envisioneer", "monetize", "harness", "facilitate", "seize", "disintermediate", "synergize", "strategize", "deploy", 
"brand", "grow", "target", "syndicate", "synthesize", "deliver", "mesh", "incubate", "engage", "maximize", "benchmark", 
"expedite", "reintermediate", "whiteboard", "visualize", "repurpose", "innovate", "scale", "unleash", "drive", "extend", 
"engineer", "revolutionize", "generate", "exploit", "transition", "e-enable", "iterate", "cultivate", "matrix", 
"productize", "redefine", 
"recontextualize"]

_DIGENERATOR_ADJECTIVES = ["clicks-and-mortar", "value-added", "vertical", "proactive", "robust", "revolutionary", "scalable", "resourcefull"
"leading-edge", "innovative", "intuitive", "strategic", "e-business", "mission-critical", "sticky", "one-to-one", 
"24/7", "end-to-end", "global", "B2B", "wearable", "granular", "frictionless", "virtual", "viral", "dynamic", "24/365", 
"best-of-breed", "killer", "magnetic", "bleeding-edge", "web-enabled", "interactive", "dot-com", "sexy", "back-end", 
"real-time", "efficient", "front-end", "distributed", "seamless", "extensible", "turn-key", "world-class", "complex",
"open-source", "cross-platform", "cross-media", "synergistic", "bricks-and-clicks", "out-of-the-box", "enterprise", 
"integrated", "impactful", "wireless", "transparent", "next-generation", "cutting-edge", "user-centric", "visionary", "cloud-based",
"customized", "ubiquitous", "plug-and-play", "collaborative", "compelling", "holistic", "rich"]

_DIGENERATOR_NOUNS = ["synergies", "web-readiness", "paradigms", "markets", "partnerships", "infrastructures", "platforms", 
"initiatives", "channels", "eyeballs", "communities", "hashtags", "solutions", "e-tailers", "e-services", "action-items", 
"portals", "niches", "technologies", "content", "vortals", "supply-chains", "convergence", "relationships", 
"architectures", "interfaces", "e-markets", "e-commerce", "systems", "bandwidth", "infomediaries", "models", 
"mindshare", "deliverables", "users", "schemas", "networks", "applications", "metrics", "e-business", "functionalities", 
"experiences", "web services", "methodologies", "kubernetes technologies", "CI/CD algorithms", "ML based softwares", "microservices", "micromodules", "hosting products", "IOT concepts"]


### FUNCTIONS ###
def send_email(port, smtp_server, sender_email, receiver_email, password, email_content):
    """
    """
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, email_content)
        server.quit()


def build_email_content(client_subject, client_email, client_interest, client_message):
    """
    """
    return """Subject: DigitalML Website ContactUs - {subject}\n\n
    Client Subject: {subject}\n
    Client Email: {email}\n
    Client Interest: {interest}\n
    Client Message: {message}\n""".format(subject=client_subject, email=client_email, interest=client_interest, message=client_message)


def digenerate_product_description():
    """
    """
    return random.choice(_DIGENERATOR_VERBS) + " " + random.choice(_DIGENERATOR_ADJECTIVES) + " " + random.choice(_DIGENERATOR_NOUNS)


def digenerate_product_name():
    """
    """
    return random.choice(_DIGENERATOR_NAMES)

