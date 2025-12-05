# from sqlalchemy import inspect
# from db_utils import ENGINE
# from models import DimDepartment

# # Get actual database columns
# inspector = inspect(ENGINE)
# db_columns = inspector.get_columns('dim_department')

# print("=" * 60)
# print("DATABASE TABLE COLUMNS:")
# print("=" * 60)
# for col in db_columns:
#     print(f"  - {col['name']} ({col['type']})")

# print("\n" + "=" * 60)
# print("MODEL COLUMNS:")
# print("=" * 60)
# for col in DimDepartment.__table__.columns:
#     print(f"  - {col.name} ({col.type})")

# print("\n" + "=" * 60)
# print("COMPARISON:")
# print("=" * 60)
# db_col_names = {col['name'] for col in db_columns}
# model_col_names = {col.name for col in DimDepartment.__table__.columns}

# missing_in_db = model_col_names - db_col_names
# missing_in_model = db_col_names - model_col_names

# if missing_in_db:
#     print(f" Columns in model but NOT in database: {missing_in_db}")
# if missing_in_model:
#     print(f" Columns in database but NOT in model: {missing_in_model}")
# if not missing_in_db and not missing_in_model:
#     print("Schema matches perfectly!")
