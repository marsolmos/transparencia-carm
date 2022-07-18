import unidecode


def to_camel_case(text):
    '''
    Function to camel-case the given input string

    :return: input string as camel-case
    :rtype: string
    '''
    s = text.replace("-", " ").replace("_", " ").replace("\n", " ")
    s = s.split()
    if len(text) == 0:
        return text
    return ' '.join(i.capitalize() for i in s[0:])


def normalize_string(text):
    '''
    Function to normailze the given input string:
        - Camel-case
        - Remove accents
    :return: input string normalized
    :rtype: string
    '''
    accented_string = to_camel_case(text)
    normalized_string = unidecode.unidecode(accented_string)

    return normalized_string


def normalize_institutions(inst):
    '''
    Normalize instituions names

    :param inst: input name of the institution to be normalized
    :type inst: string
    :return: normalized name of the given institution
    :rtype: string
    '''
    # Check if the institution is a Consejeria
    if "C. De " in inst:
        if "salud"  in inst.lower():
            normalized_inst = "Consejeria de Salud"
        elif "fomento" in inst.lower():
            normalized_inst = "Consejeria de Fomento e Infraestructuras"
        elif "hacienda" in inst.lower():
            normalized_inst = "Consejeria de Economía, Hacienda y Administración Digital"
        elif "empleo" in inst.lower():
            normalized_inst = "Consejeria de Empresa, Empleo, Universidades y Portavocía"
        elif "educacion" in inst.lower():
            normalized_inst = "Consejeria de Educacion"
        elif "turismo" or "cultura" or "deportes" in inst.lower():
            normalized_inst = "Consejeria de Presidencia, Turismo, Cultura y Deportes"
        elif "igualdad" or "mujer" or "lgtb" or "transparencia" in inst.lower():
            normalized_inst = "Consejeria de Mujer, Igualdad, LGTBI, Familias, Política Social y Transparencia. Vicepresidencia"
        else:
            normalized_inst = f"Consejeria Desconocida: ({inst})"
    # Check if the institution is a Instituto
    elif "instituto" in inst.lower():
        if "credito" in inst.lower():
            normalized_inst = "Instituto De Credito Y Finanzas De La Region De Murcia"
        elif "fomento" in inst.lower():
            normalized_inst = "Instituto De Fomento De La Region De Murcia"
        else:
            normalized_inst = inst
    elif "i.m.a.s" in inst.lower():
        normalized_inst = "Instituto Murciano de Accion Social"
    elif "i.m.i.d.a" in inst.lower():
        normalized_inst = "Instituto Murciano de Investigacion y Desarrollo Agrario y Medioambiental"
    # Check other cases
    elif "sms" in inst.lower():
        normalized_inst = "Servicios Centrales (SMS)"
    elif "informatica" in inst.lower():
        normalized_inst = "Direccion General de Patrimonio"
    elif "esamur" in inst.lower():
        normalized_inst = "Entidad de Saneamiento y Depuracion de Aguas Residuales de la Region de Murcia"
    # If no case found, then return the original institution name
    else:
        normalized_inst = inst
    return normalized_inst