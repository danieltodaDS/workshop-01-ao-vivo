import pandas as pd
from contrato import Vendas

def process_excel(uploaded_file): 
    try:
        df = pd.read_excel(uploaded_file)

        extra_cols = set(df.columns) - set(Vendas.model_fields.keys())
        if extra_cols:
            return False, f"Colunas extras detectadas no excel: {','.join(extra_cols)}"
        
        for index, row in df.iterrows(): 
            try:
                _ = Vendas(**row.to_dict())
            except Exception as e: 
                raise ValueError (f"Erro na linha {index+2}:{e}")
        
        return df, True, None

            
    except ValueError as ve:
        return df, False, str(ve)
    except Exception as e:
        return df, False, f"Erro inesperado: {str(e)}"