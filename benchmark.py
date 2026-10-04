import time
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score, precision_score, recall_score
import lightgbm as lgb
import os

def main():
    results = {}
    
    # 1. Load data
    start_time = time.time()
    csv_path = os.path.expanduser('~/ml-benchmark/creditcard.csv')
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found. Ensure dataset is downloaded and extracted.")
        return
        
    df = pd.read_csv(csv_path)
    X = df.drop('Class', axis=1)
    y = df['Class']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    load_time = time.time() - start_time
    results['Thời gian load data'] = f"{load_time:.4f} seconds"
    
    # 2. Train model
    start_time = time.time()
    model = lgb.LGBMClassifier(random_state=42, n_estimators=100)
    model.fit(X_train, y_train, eval_set=[(X_test, y_test)], eval_metric='auc')
    train_time = time.time() - start_time
    results['Thời gian training'] = f"{train_time:.4f} seconds"
    results['Best iteration'] = model.best_iteration_ if model.best_iteration_ else 100
    
    # 3. Evaluation
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    
    results['AUC-ROC'] = float(roc_auc_score(y_test, y_prob))
    results['Accuracy'] = float(accuracy_score(y_test, y_pred))
    results['F1-Score'] = float(f1_score(y_test, y_pred))
    results['Precision'] = float(precision_score(y_test, y_pred))
    results['Recall'] = float(recall_score(y_test, y_pred))
    
    # 4. Inference Latency & Throughput
    single_row = X_test.iloc[[0]]
    start_time = time.time()
    model.predict(single_row)
    latency = time.time() - start_time
    results['Inference latency (1 row)'] = f"{latency:.6f} seconds"
    
    thousand_rows = X_test.iloc[:1000]
    start_time = time.time()
    model.predict(thousand_rows)
    throughput_time = time.time() - start_time
    results['Inference throughput (1000 rows)'] = f"{throughput_time:.6f} seconds"
    
    # Write to JSON
    with open('benchmark_result.json', 'w') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
        
    print("Benchmark completed. Results saved to benchmark_result.json.")
    print(json.dumps(results, indent=4, ensure_ascii=False))

if __name__ == '__main__':
    main()
