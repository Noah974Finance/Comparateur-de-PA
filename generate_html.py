import json
import os

def build_html():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'PA_DATA.json')
    prix_file_path = os.path.join(current_dir, 'prix.json')

    with open(file_path, 'r', encoding='utf-8') as f:
        pa_data = json.load(f)

    with open(prix_file_path, 'r', encoding='utf-8') as f:
        prix_data = json.load(f)

    # Sort PAs by name alphabetically
    pa_data.sort(key=lambda x: x["name"].upper())

    # Build the HTML template
    html_template = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comparateur PA — Plateformes Agréées Facturation Électronique 2026</title>
    <meta name="description" content="Comparateur exhaustif des 47 Plateformes Agréées pour la facturation électronique en France. Comparez tous les critères techniques, tarifs et services.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-primary: #080b11;
            --bg-secondary: #0f131a;
            --bg-card: #151922;
            --bg-card-hover: #1c212d;
            --bg-glass: rgba(21, 25, 34, 0.75);
            --border: rgba(99, 102, 241, 0.12);
            --border-hover: rgba(99, 102, 241, 0.3);
            --text-primary: #f3f4f6;
            --text-secondary: #9ca3af;
            --text-dim: #6b7280;
            
            --accent: #6366f1;
            --accent-hover: #4f46e5;
            --accent-glow: rgba(99, 102, 241, 0.25);
            
            --green: #10b981;
            --green-dim: rgba(16, 185, 129, 0.15);
            --red: #ef4444;
            --red-dim: rgba(239, 68, 68, 0.15);
            
            --gradient-hero: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
            --radius-lg: 16px;
            --radius-md: 12px;
            --radius-sm: 8px;
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
            background-color: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            line-height: 1.5;
            overflow-x: hidden;
        }

        /* Scrollbars custom */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: var(--bg-primary);
        }
        ::-webkit-scrollbar-thumb {
            background: var(--border-hover);
            border-radius: 99px;
        }

        /* ── Top Nav ── */
        .top-nav {
            position: sticky; top: 0; z-index: 200;
            background: rgba(8,11,17,.88); backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border);
            display: flex; align-items: center; justify-content: space-between;
            padding: 0 24px; height: 52px;
        }
        .top-nav-brand {
            font-family: 'Outfit', sans-serif; font-weight: 800; font-size: .9rem;
            background: var(--gradient-hero); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            letter-spacing: -.02em;
        }
        .top-nav-tabs { display: flex; gap: 2px; }
        .top-nav-tab {
            padding: 6px 14px; border-radius: 7px; font-size: .78rem; font-weight: 600;
            color: var(--text-secondary); cursor: pointer; border: none; background: none;
            transition: var(--transition); text-decoration: none;
        }
        .top-nav-tab:hover, .top-nav-tab.active { background: rgba(99,102,241,.15); color: #a5b4fc; }
        .top-nav-tab.active { color: #c7d2fe; }
        .top-nav-btn {
            display: flex; align-items: center; gap: 6px;
            padding: 7px 15px; border-radius: 8px; font-size: .78rem; font-weight: 700;
            background: rgba(99,102,241,.12); border: 1px solid rgba(99,102,241,.28); color: #a5b4fc;
            cursor: pointer; text-decoration: none; transition: var(--transition);
        }
        .top-nav-btn:hover { background: rgba(99,102,241,.22); border-color: rgba(99,102,241,.5); }

        /* Header / Hero */
        .hero {
            position: relative;
            padding: 60px 24px 40px;
            text-align: center;
            background: radial-gradient(circle at top, rgba(99, 102, 241, 0.15) 0%, transparent 60%);
            border-bottom: 1px solid var(--border);
        }

        .badge-update {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(99, 102, 241, 0.15);
            border: 1px solid rgba(99, 102, 241, 0.3);
            color: #a5b4fc;
            padding: 6px 14px;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-bottom: 16px;
        }

        .badge-update span {
            width: 8px;
            height: 8px;
            background: var(--green);
            border-radius: 50%;
            display: inline-block;
            box-shadow: 0 0 10px var(--green);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(0.9); opacity: 0.6; }
            50% { transform: scale(1.2); opacity: 1; }
            100% { transform: scale(0.9); opacity: 0.6; }
        }

        .hero h1 {
            font-family: 'Outfit', sans-serif;
            font-size: clamp(2.2rem, 5vw, 3.8rem);
            font-weight: 900;
            letter-spacing: -0.03em;
            background: var(--gradient-hero);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 12px;
        }

        .hero p {
            font-size: clamp(1rem, 2vw, 1.25rem);
            color: var(--text-secondary);
            max-width: 800px;
            margin: 0 auto;
        }

        /* Layout */
        .container {
            max-width: 1440px;
            margin: 0 auto;
            padding: 30px 24px;
            display: grid;
            grid-template-columns: 280px 1fr;
            gap: 24px;
        }

        @media (max-width: 1024px) {
            .container {
                grid-template-columns: 1fr;
            }
        }

        /* Sidebar / Filters (With fixed layout scroll logic) */
        .filters-sidebar {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 18px;
            position: sticky;
            top: 24px;
            max-height: calc(100vh - 48px);
            overflow-y: auto;
            align-self: start; /* Prevents grid stretching */
        }

        .filter-section {
            margin-bottom: 20px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            padding-bottom: 16px;
        }

        .filter-section:last-child {
            margin-bottom: 0;
            border-bottom: none;
            padding-bottom: 0;
        }

        .filter-title {
            font-family: 'Outfit', sans-serif;
            font-size: 0.9rem;
            font-weight: 700;
            color: #a5b4fc;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 14px;
        }

        .filter-options {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .filter-checkbox {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 0.85rem;
            color: var(--text-secondary);
            cursor: pointer;
            user-select: none;
            transition: var(--transition);
        }

        .filter-checkbox:hover {
            color: var(--text-primary);
        }

        .filter-checkbox input {
            appearance: none;
            width: 16px;
            height: 16px;
            border: 1.5px solid var(--border-hover);
            border-radius: 4px;
            background: rgba(255, 255, 255, 0.02);
            cursor: pointer;
            position: relative;
            transition: var(--transition);
            flex-shrink: 0;
        }

        .filter-checkbox input:checked {
            background: var(--accent);
            border-color: var(--accent);
        }

        .filter-checkbox input:checked::after {
            content: "✓";
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            font-size: 10px;
            font-weight: 900;
        }

        /* Content Area */
        .content-area {
            display: flex;
            flex-direction: column;
            gap: 24px;
        }

        /* Search bar */
        .search-container {
            position: relative;
        }

        .search-input {
            width: 100%;
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 16px 20px 16px 52px;
            color: var(--text-primary);
            font-family: inherit;
            font-size: 1rem;
            transition: var(--transition);
        }

        .search-input:focus {
            outline: none;
            border-color: var(--accent-hover);
            box-shadow: 0 0 20px var(--accent-glow);
        }

        .search-icon {
            position: absolute;
            left: 20px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-dim);
            font-size: 1.2rem;
            pointer-events: none;
        }

        /* Statistics bar */
        .quick-stats {
            display: flex;
            gap: 16px;
            flex-wrap: wrap;
        }

        .stat-badge {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 12px 20px;
            flex: 1;
            min-width: 180px;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .stat-value {
            font-family: 'Outfit', sans-serif;
            font-size: 1.5rem;
            font-weight: 800;
            color: #a5b4fc;
        }

        .stat-label {
            font-size: 0.8rem;
            color: var(--text-secondary);
        }

        /* Grid Layout Selector */
        .search-controls-container {
            display: flex;
            gap: 16px;
            align-items: center;
            width: 100%;
        }

        .layout-selector {
            display: flex;
            gap: 4px;
            background: var(--bg-card);
            border: 1px solid var(--border);
            padding: 4px;
            border-radius: var(--radius-md);
            align-items: center;
        }

        .layout-label {
            font-size: 0.72rem;
            color: var(--text-dim);
            margin: 0 8px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            white-space: nowrap;
        }

        .layout-btn {
            background: transparent;
            border: none;
            color: var(--text-secondary);
            cursor: pointer;
            padding: 6px 12px;
            border-radius: var(--radius-sm);
            font-size: 0.85rem;
            font-weight: 600;
            transition: var(--transition);
        }

        .layout-btn:hover {
            color: var(--text-primary);
            background: rgba(255, 255, 255, 0.03);
        }

        .layout-btn.active {
            background: var(--accent);
            color: white;
        }

        @media (max-width: 768px) {
            .search-controls-container {
                flex-direction: column;
                align-items: stretch;
            }
            .layout-selector {
                justify-content: center;
            }
        }

        /* PAs Grid */
        .pas-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
            gap: 20px;
        }

        @media (min-width: 1025px) {
            .pas-grid.cols-2 { grid-template-columns: repeat(2, 1fr) !important; }
            .pas-grid.cols-3 { grid-template-columns: repeat(3, 1fr) !important; }
            .pas-grid.cols-4 { grid-template-columns: repeat(4, 1fr) !important; }
        }

        .pa-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 24px;
            display: flex;
            flex-direction: column;
            position: relative;
            transition: var(--transition);
            min-width: 0;
        }

        .pa-card:hover {
            transform: translateY(-4px);
            border-color: var(--border-hover);
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        }

        /* Header row in card */
        .pa-card-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 16px;
            margin-bottom: 10px;
        }

        .pa-name {
            font-family: 'Outfit', sans-serif;
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--text-primary);
            line-height: 1.3;
            min-width: 0;
            word-wrap: break-word;
        }

        /* Checkbox inside Card for comparison selection */
        .select-compare-container {
            flex-shrink: 0;
        }

        .select-compare-label {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 0.8rem;
            color: var(--text-dim);
            cursor: pointer;
            user-select: none;
            transition: var(--transition);
        }

        .select-compare-label:hover {
            color: var(--text-primary);
        }

        .select-compare-checkbox {
            appearance: none;
            width: 16px;
            height: 16px;
            border: 1.5px solid var(--border-hover);
            border-radius: 4px;
            background: rgba(255, 255, 255, 0.02);
            cursor: pointer;
            position: relative;
            transition: var(--transition);
        }

        .select-compare-checkbox:checked {
            background: var(--accent);
            border-color: var(--accent);
        }

        .select-compare-checkbox:checked::after {
            content: "✓";
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            font-size: 10px;
            font-weight: 900;
        }

        .pa-desc {
            font-size: 0.88rem;
            color: var(--text-secondary);
            margin-bottom: 16px;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
            text-overflow: ellipsis;
            line-height: 1.5;
            flex-grow: 1;
        }

        .pa-tags {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-bottom: 16px;
        }

        .pa-tag {
            font-size: 0.72rem;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 6px;
            text-transform: uppercase;
        }

        .pa-tag-cabinet {
            background: rgba(16, 185, 129, 0.12);
            color: #34d399;
            border: 1px solid rgba(16, 185, 129, 0.3);
        }

        .pa-tag-independent {
            background: rgba(99, 102, 241, 0.12);
            color: #818cf8;
            border: 1px solid rgba(99, 102, 241, 0.3);
        }

        .pa-tag-cible {
            background: rgba(245, 158, 11, 0.12);
            color: #fbbf24;
            border: 1px solid rgba(245, 158, 11, 0.3);
        }

        /* Cleaned card metadata layout */
        .pa-meta-summary {
            padding: 16px 0;
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
            margin-bottom: 18px;
            display: flex;
            flex-direction: column;
            gap: 12px;
            min-width: 0;
        }

        .pa-meta-tarif-row {
            display: flex;
            flex-direction: column;
            gap: 4px;
            min-width: 0;
        }

        .pa-meta-val-long {
            font-size: 0.88rem;
            color: var(--text-primary);
            font-weight: 600;
            line-height: 1.4;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .pa-badges-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
            min-width: 0;
        }

        .pa-badge-item {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 0.8rem;
            font-weight: 600;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            min-width: 0;
        }

        .pa-badge-yes {
            color: var(--green);
        }

        .pa-badge-no {
            color: var(--text-dim);
            opacity: 0.7;
        }

        .pa-meta-lbl {
            font-size: 0.72rem;
            color: var(--text-dim);
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 0.05em;
        }

        .pa-actions {
            display: flex;
            gap: 10px;
            margin-top: auto;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 10px 16px;
            border-radius: var(--radius-sm);
            font-family: inherit;
            font-size: 0.9rem;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
            text-decoration: none;
            border: 1px solid transparent;
            width: 100%;
        }

        .btn-primary {
            background: var(--accent);
            color: white;
        }

        .btn-primary:hover {
            background: var(--accent-hover);
            box-shadow: 0 0 15px rgba(99, 102, 241, 0.4);
        }

        .btn-secondary {
            background: transparent;
            border-color: var(--border);
            color: var(--text-secondary);
        }

        .btn-secondary:hover {
            border-color: var(--border-hover);
            color: var(--text-primary);
            background: rgba(255,255,255,0.02);
        }

        /* Floating Compare Action Bar (Z-index fixed to 9999, proper translate layout) */
        .compare-bar {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translate(-50%, 150%);
            background: rgba(21, 25, 34, 0.95);
            border: 1px solid var(--accent);
            border-radius: var(--radius-md);
            padding: 16px 24px;
            display: flex;
            align-items: center;
            gap: 20px;
            z-index: 9999;
            backdrop-filter: blur(20px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.6), 0 0 20px var(--accent-glow);
            opacity: 0;
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.4s;
            pointer-events: none;
        }

        .compare-bar.show {
            transform: translate(-50%, 0);
            opacity: 1;
            pointer-events: all;
        }

        .compare-info {
            font-size: 0.95rem;
            font-weight: 600;
            color: var(--text-primary);
        }

        .compare-actions {
            display: flex;
            gap: 12px;
        }

        .btn-compare-action {
            padding: 8px 18px;
            font-size: 0.85rem;
            font-weight: 700;
            border-radius: var(--radius-sm);
        }

        /* Fullscreen Modals */
        .modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 10000; /* Higher than compare-bar */
            background: rgba(8, 11, 17, 0.95);
            backdrop-filter: blur(10px);
            display: none;
            justify-content: center;
            align-items: center;
            opacity: 0;
            transition: opacity 0.3s var(--transition);
        }

        .modal.show {
            display: flex;
            opacity: 1;
        }

        .modal-container {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            width: 95%;
            max-width: 1300px;
            height: 90%;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8);
            transform: scale(0.95);
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .modal.show .modal-container {
            transform: scale(1);
        }

        .modal-header {
            padding: 24px;
            border-bottom: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .modal-title {
            font-family: 'Outfit', sans-serif;
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--text-primary);
        }

        .modal-close {
            background: none;
            border: none;
            color: var(--text-secondary);
            font-size: 1.8rem;
            cursor: pointer;
            transition: var(--transition);
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            border-radius: 50%;
        }

        .modal-close:hover {
            color: var(--text-primary);
            background: rgba(255,255,255,0.05);
        }

        .modal-content {
            padding: 32px;
            overflow-y: auto;
            flex-grow: 1;
        }

        /* Multi Comparison Matrix Styling */
        .comparison-table-wrapper {
            overflow-x: auto;
            width: 100%;
        }

        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            text-align: left;
        }

        .comparison-table th, .comparison-table td {
            padding: 16px 20px;
            border-bottom: 1px solid var(--border);
            font-size: 0.9rem;
            vertical-align: middle;
        }

        .comparison-table th {
            background: var(--bg-secondary);
            color: var(--text-primary);
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            position: sticky;
            top: 0;
            z-index: 10;
        }

        .comparison-table .row-category {
            background: rgba(99, 102, 241, 0.05);
            font-weight: 800;
            color: #a5b4fc;
            text-transform: uppercase;
            font-size: 0.85rem;
            letter-spacing: 0.05em;
        }

        .comparison-table .row-feature-title {
            font-weight: 600;
            color: var(--text-secondary);
            width: 250px;
            min-width: 200px;
        }

        .comparison-table td {
            color: var(--text-primary);
            max-width: 300px;
            word-wrap: break-word;
        }

        .comparison-value-bool {
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 600;
        }

        .val-yes {
            color: var(--green);
        }

        .val-no {
            color: var(--red);
        }

        /* Detail Card Grid layout */
        .detail-grid {
            display: grid;
            grid-template-columns: 1fr 380px;
            gap: 32px;
        }

        @media (max-width: 768px) {
            .detail-grid {
                grid-template-columns: 1fr;
            }
        }

        .detail-main {
            display: flex;
            flex-direction: column;
            gap: 24px;
        }

        .detail-sidebar {
            display: flex;
            flex-direction: column;
            gap: 24px;
        }

        .detail-card-box {
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 24px;
        }

        .detail-card-box h3 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.1rem;
            font-weight: 700;
            color: #a5b4fc;
            margin-bottom: 16px;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            padding-bottom: 8px;
        }

        .detail-field-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .detail-field-item {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 20px;
            padding-bottom: 8px;
            border-bottom: 1px solid rgba(255,255,255,0.02);
            font-size: 0.9rem;
        }

        .detail-field-item:last-child {
            border-bottom: none;
            padding-bottom: 0;
        }

        .detail-field-name {
            color: var(--text-secondary);
            font-weight: 500;
        }

        .detail-field-value {
            font-weight: 600;
            color: var(--text-primary);
            text-align: right;
            max-width: 60%;
            word-wrap: break-word;
        }

        /* Atouts lists */
        .atouts-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .atouts-item {
            display: flex;
            align-items: flex-start;
            gap: 10px;
            font-size: 0.9rem;
            color: var(--text-primary);
            background: rgba(99, 102, 241, 0.05);
            padding: 12px 16px;
            border-radius: var(--radius-sm);
            border-left: 3px solid var(--accent);
            line-height: 1.4;
        }

        /* Custom empty state */
        .empty-state {
            grid-column: 1 / -1;
            text-align: center;
            padding: 60px 40px;
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            color: var(--text-secondary);
        }

        /* ── PAGE SWITCHER ── */
        .app-page {
            display: none;
        }
        .app-page.active {
            display: block;
        }

        /* ── STATS (Tarifs Page) ── */
        .stats-row {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            justify-content: center;
            padding: 20px 24px;
            border-bottom: 1px solid var(--border);
            background: var(--bg-secondary);
        }
        .stat-box {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 3px;
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 12px 20px;
            min-width: 120px;
        }
        .stat-box-val { font-family: 'Outfit', sans-serif; font-size: 1.75rem; font-weight: 900; line-height: 1; }
        .stat-box-lbl { font-size: .7rem; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: var(--text-dim); }
        .c-green  { color: var(--green); }
        .c-amber  { color: #fbbf24; }
        .c-blue   { color: #3b82f6;  }
        .c-purple { color: #a855f7;}
        .c-accent { color: var(--accent);}

        /* ── CONTROLS (Tarifs Page) ── */
        .tarifs-controls {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            align-items: center;
            padding: 18px 24px;
        }
        .tarifs-search-wrap { position: relative; flex: 1; min-width: 220px; }
        .tarifs-search-icon { position: absolute; left: 14px; top: 50%; transform: translateY(-50%); color: var(--text-dim); font-size: .95rem; pointer-events: none; }
        .tarifs-search-inp {
            width: 100%;
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 10px 14px 10px 40px;
            color: var(--text-primary);
            font-family: inherit;
            font-size: .87rem;
            outline: none;
            transition: var(--transition);
        }
        .tarifs-search-inp::placeholder { color: var(--text-dim); }
        .tarifs-search-inp:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-glow); }
        
        .tarifs-chips { display: flex; gap: 6px; flex-wrap: wrap; }
        .tarifs-chip {
            padding: 8px 14px; border-radius: 7px; font-size: .78rem; font-weight: 700;
            border: 1px solid var(--border); background: var(--bg-card); color: var(--text-secondary);
            cursor: pointer; transition: var(--transition);
        }
        .tarifs-chip:hover { border-color: var(--accent); color: #a5b4fc; }
        .tarifs-chip.on { background: var(--accent-glow); border-color: var(--accent); color: #c7d2fe; }
        
        .tarifs-sort-sel {
            background: var(--bg-card); border: 1px solid var(--border); color: var(--text-secondary);
            padding: 8px 13px; border-radius: 7px; font-size: .78rem; font-weight: 600;
            font-family: inherit; cursor: pointer; outline: none;
        }
        .tarifs-count { color: var(--text-dim); font-size: .78rem; font-weight: 700; padding: 8px 4px; white-space: nowrap; }

        /* ── SECTION HEADER ── */
        .tarifs-section-hdr {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 24px 24px 10px;
            font-family: 'Outfit', sans-serif;
            font-size: .92rem;
            font-weight: 800;
            color: var(--text-primary);
        }
        .tarifs-section-hdr::after { content:''; flex:1; height:1px; background: var(--border); }

        /* ── CALENDRIER ── */
        .tarifs-cal-row {
            max-width: 1400px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            padding: 0 24px;
        }
        @media(max-width:768px){ .tarifs-cal-row { grid-template-columns: 1fr; } }
        .tarifs-cal-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 18px;
            text-align: center;
        }
        .tarifs-cal-date { font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 800; color: var(--accent); margin-bottom: 6px; }
        .tarifs-cal-lbl { font-size: .8rem; color: var(--text-secondary); line-height: 1.5; }

        /* ── SYNTHESE ── */
        .tarifs-synth-row {
            max-width: 1400px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
            gap: 12px;
            padding: 0 24px;
        }
        .tarifs-synth-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 18px;
        }
        .tarifs-synth-title {
            font-family: 'Outfit', sans-serif; font-size: .75rem; font-weight: 800;
            color: #a5b4fc; text-transform: uppercase; letter-spacing: .06em; margin-bottom: 12px;
        }
        .tarifs-synth-list { display: flex; flex-direction: column; gap: 6px; }
        .tarifs-synth-item { display: flex; align-items: flex-start; gap: 8px; font-size: .8rem; color: var(--text-secondary); }
        .tarifs-bullet { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; margin-top: 5px; }
        .tarifs-b-green  { background: var(--green); }
        .tarifs-b-blue   { background: #3b82f6;  }
        .tarifs-b-amber  { background: #f59e0b; }
        .tarifs-b-gray   { background: var(--text-dim); }
        .tarifs-synth-item strong { color: var(--text-primary); }

        /* ── GRID ── */
        .tarifs-grid {
            max-width: 1400px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
            gap: 16px;
            padding: 0 24px 60px;
        }

        /* ── CARD ── */
        .t-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 0;
            position: relative;
            overflow: hidden;
            transition: var(--transition);
        }
        .t-card::before {
            content:'';
            position: absolute;
            top:0; left:0; right:0; height: 2px;
            background: var(--gradient-hero);
            opacity: 0;
            transition: opacity .3s;
        }
        .t-card:hover { border-color: var(--border-hover); transform: translateY(-2px); box-shadow: 0 10px 32px rgba(0,0,0,.5); }
        .t-card:hover::before { opacity: 1; }

        .t-badge {
            position: absolute; top: 14px; right: 14px;
            font-size: .65rem; font-weight: 800; padding: 3px 9px; border-radius: 6px;
            text-transform: uppercase; letter-spacing: .05em;
        }
        .t-badge-free    { background: var(--green-dim);  color: #34d399; border: 1px solid rgba(16,185,129,.22);  }
        .t-badge-paid    { background: rgba(59,130,246,.10);   color: #60a5fa; border: 1px solid rgba(59,130,246,.22);   }
        .t-badge-devis   { background: rgba(107,114,128,.10);   color: #9ca3af; border: 1px solid rgba(107,114,128,.22);   }
        .t-badge-freemium{ background: rgba(168,85,247,.10); color: #c084fc; border: 1px solid rgba(168,85,247,.22); }

        .t-card-name {
            font-family: 'Outfit', sans-serif; font-size: 1rem; font-weight: 800;
            color: var(--text-primary); line-height: 1.25; padding-right: 72px; margin-bottom: 2px;
        }
        .t-card-offre { font-size: .75rem; color: var(--text-dim); margin-bottom: 12px; }

        .t-card-price { font-family: 'Outfit', sans-serif; font-size: 1.5rem; font-weight: 900; line-height: 1; }
        .t-card-price-type { font-size: .72rem; color: var(--text-dim); font-weight: 600; margin-top: 3px; margin-bottom: 14px; }
        .t-p-free    { color: var(--green);  }
        .t-p-paid    { color: #3b82f6;   }
        .t-p-devis   { color: var(--text-secondary); font-size: 1.1rem; }
        .t-p-freemium{ color: #a855f7; }

        .t-card-cible {
            display: flex; align-items: center; gap: 6px; margin-bottom: 12px;
            font-size: .76rem; color: var(--text-dim);
        }

        .t-card-site {
            display: flex; align-items: center; gap: 6px; margin-bottom: 12px;
            font-size: .74rem;
        }
        .t-card-site a {
            color: #a5b4fc; text-decoration: none; transition: color .2s;
            overflow: hidden; text-overflow: ellipsis; white-space: nowrap; max-width: 220px;
        }
        .t-card-site a:hover { color: #c7d2fe; text-decoration: underline; }

        .t-offers { margin-bottom: 12px; }
        .t-offers-lbl { font-size: .68rem; font-weight: 800; text-transform: uppercase; letter-spacing: .06em; color: var(--text-dim); margin-bottom: 7px; }
        .t-offer-item {
            display: flex; justify-content: space-between; align-items: center;
            background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.04);
            border-radius: 7px; padding: 7px 11px; margin-bottom: 5px;
            font-size: .76rem; gap: 8px;
        }
        .t-offer-item:last-child { margin-bottom: 0; }
        .t-offer-name { color: var(--text-secondary); font-weight: 600; }
        .t-offer-price { color: var(--text-primary); font-weight: 700; text-align: right; }
        .t-offer-reduce { color: var(--green); font-size: .7rem; font-weight: 700; }

        .t-feats-lbl { font-size: .68rem; font-weight: 800; text-transform: uppercase; letter-spacing: .06em; color: var(--text-dim); margin-bottom: 7px; }
        .t-feats { display: flex; flex-direction: column; gap: 4px; flex: 1; }
        .t-feat { display: flex; align-items: flex-start; gap: 7px; font-size: .79rem; color: var(--text-secondary); line-height: 1.4; }
        .t-feat-check { color: var(--green); font-size: .7rem; margin-top: 2px; flex-shrink: 0; }

        .t-formats { display: flex; gap: 5px; flex-wrap: wrap; margin-top: 12px; padding-top: 12px; border-top: 1px solid rgba(255,255,255,.05); }
        .t-fmt {
            font-size: .65rem; font-weight: 700; padding: 3px 8px; border-radius: 5px;
            background: var(--accent-glow); color: #a5b4fc; border: 1px solid rgba(99,102,241,.2);
        }

        .t-card-foot { display: flex; justify-content: space-between; align-items: center; margin-top: 10px; flex-wrap: wrap; gap: 4px; }
        .t-card-note { font-size: .72rem; color: #f59e0b; font-weight: 700; }
        .t-card-trial { font-size: .7rem; color: var(--green); font-weight: 700; background: var(--green-dim); padding: 3px 9px; border-radius: 6px; }
        .t-card-no-site { font-size: .7rem; color: var(--text-dim); font-style: italic; }

        .t-card-contact { font-size: .7rem; color: var(--text-dim); margin-bottom: 10px; }
    </style>
</head>
<body>

    <!-- TOP NAV -->
    <nav class="top-nav">
        <span class="top-nav-brand">⚡ Comparateur PA</span>
        <div class="top-nav-tabs">
            <a href="#" class="top-nav-tab active" data-page="comparateur" onclick="showPage('comparateur'); return false;">🔍 Comparateur</a>
            <a href="#" class="top-nav-tab" data-page="tarifs" onclick="showPage('tarifs'); return false;">💶 Tarifs</a>
        </div>
        <a href="#" class="top-nav-btn" onclick="showPage('tarifs'); return false;">💶 Voir les tarifs →</a>
    </nav>

    <!-- ── PAGE COMPARATEUR ── -->
    <div id="page-comparateur" class="app-page active">
        <!-- HERO -->
        <header class="hero">
        <div class="badge-update">
            <span></span>
            Base de données mise à jour — Juin 2026
        </div>
        <h1>Comparateur de Plateformes Agréées (PA)</h1>
        <p>Comparez les 47 PAs officiellement référencées et analysez l'intégralité de leurs critères réglementaires, techniques et structurels.</p>
    </header>

    <!-- CONTENT CONTAINER -->
    <main class="container">
        
        <!-- SIDEBAR FILTERS -->
        <aside class="filters-sidebar">
            <div class="filter-section">
                <div class="filter-title">Type de Cible</div>
                <div class="filter-options">
                    <label class="filter-checkbox">
                        <input type="checkbox" class="target-filter" value="TPE"> TPE
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" class="target-filter" value="PME"> PME
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" class="target-filter" value="ETI"> ETI
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" class="target-filter" value="GE"> GE
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" class="target-filter" value="International"> International
                    </label>
                </div>
            </div>

            <div class="filter-section">
                <div class="filter-title">Profil & Usage</div>
                <div class="filter-options">
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-cabinet"> Usage Cabinet Experts
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-suite"> Intégration Suite Logicielle
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-immatriculation"> Agrément / Immatriculée DGFIP
                    </label>
                </div>
            </div>

            <div class="filter-section">
                <div class="filter-title">Service de Paiement</div>
                <div class="filter-options">
                    <label class="filter-checkbox">
                        <input type="checkbox" class="payment-filter" value="traditionnelle"> Banque traditionnelle
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" class="payment-filter" value="neobanque"> Néobanque
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" class="payment-filter" value="aucun"> Aucun service de paiement
                    </label>
                </div>
            </div>

            <div class="filter-section">
                <div class="filter-title">Modèle Tarifaire</div>
                <div class="filter-options">
                    <label class="filter-checkbox">
                        <input type="checkbox" class="pricing-filter" value="gratuit"> 100% Gratuit / Inclus
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" class="pricing-filter" value="abonnement"> Abonnement / Forfait fixe
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" class="pricing-filter" value="volume"> Facturation au volume / usage
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-maintenance"> Maintenance & Hotline incluses
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-maj-gratuite"> Mises à jour gratuites
                    </label>
                </div>
            </div>

            <div class="filter-section">
                <div class="filter-title">Formats & E-reporting</div>
                <div class="filter-options">
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-facturx"> Création Factur-X
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-cii"> Création CII
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-ubl"> Création UBL
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-saisie"> Saisie en ligne des factures
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-wf-facture"> Workflow validation factures
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-wf-paiement"> Workflow validation paiements
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-ereporting"> Génération e-Reporting normé
                    </label>
                </div>
            </div>

            <div class="filter-section">
                <div class="filter-title">Réseaux & Protocoles</div>
                <div class="filter-options">
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-peppol"> Réseau PEPPOL
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-api"> APIs disponibles
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-reversibilite"> Réversibilité simple (changement PA)
                    </label>
                </div>
            </div>

            <div class="filter-section">
                <div class="filter-title">Services Complémentaires</div>
                <div class="filter-options">
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-ocr"> Module OCR intégré
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-archivage"> Archivage valeur probatoire
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-rapprochement"> Rapprochement paiements
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-relances"> Relances factures clients
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-signature"> Signature / Scellement
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-tableau"> Tableaux de bord de suivi
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-controle-validite"> Contrôle de validité des infos
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-gescom"> Gestion commerciale complète
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-financement"> Financement de factures
                    </label>
                </div>
            </div>

            <div class="filter-section">
                <div class="filter-title">Sécurité & Support</div>
                <div class="filter-options">
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-iso"> Certification ISO 27001
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-cloud"> Accès Cloud / SaaS
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-mobile"> Application mobile disponible
                    </label>
                    <label class="filter-checkbox">
                        <input type="checkbox" id="filter-france"> Support situé en France
                    </label>
                </div>
            </div>
        </aside>

        <!-- MAIN CONTENT AREA -->
        <section class="content-area">
            
            <!-- SEARCH & CONTROLS BAR -->
            <div class="search-controls-container">
                <div class="search-container" style="position: relative; flex-grow: 1;">
                    <span class="search-icon">🔍</span>
                    <input type="text" id="search-bar" class="search-input" placeholder="Rechercher une plateforme agréée par son nom ou mot clé...">
                </div>
                <div class="layout-selector">
                    <span class="layout-label">Colonnes</span>
                    <button class="layout-btn active" data-cols="auto">Auto</button>
                    <button class="layout-btn" data-cols="2">2</button>
                    <button class="layout-btn" data-cols="3">3</button>
                    <button class="layout-btn" data-cols="4">4</button>
                </div>
            </div>

            <!-- STATISTICS -->
            <div class="quick-stats">
                <div class="stat-badge">
                    <span class="stat-value" id="count-total">47</span>
                    <span class="stat-label">Total Plateformes</span>
                </div>
                <div class="stat-badge">
                    <span class="stat-value" id="count-cabinet">0</span>
                    <span class="stat-label">Profil Cabinet Comptable</span>
                </div>
                <div class="stat-badge">
                    <span class="stat-value" id="count-peppol">0</span>
                    <span class="stat-label">Membres Peppol</span>
                </div>
            </div>

            <!-- CARDS GRID -->
            <div class="pas-grid" id="pas-grid">
                <!-- Dynamically generated -->
            </div>
        </section>
    </main>
    </div> <!-- End of page-comparateur -->

    <!-- ── PAGE TARIFS ── -->
    <div id="page-tarifs" class="app-page">
        <!-- HERO -->
        <header class="hero">
            <div class="hero-chip"><span class="dot"></span>Sources officielles — Juin 2026</div>
            <h1>Tarifs des Plateformes Agréées</h1>
            <p class="hero-sub">Grilles tarifaires des 47 PAs référencées par la DGFiP, collectées directement sur les sites officiels de chaque entreprise.</p>
            <div class="hero-notice">
                ⚠️ <span>Données issues des sites officiels de chaque PA (pas de comparateurs tiers). Les tarifs non publics sont indiqués « Sur devis ». Pour les prix exacts, contactez directement l'entreprise.</span>
            </div>
        </header>

        <!-- STATS -->
        <div class="stats-row">
            <div class="stat-box"><span class="stat-box-val c-green" id="s-free">0</span><span class="stat-box-lbl">Gratuites</span></div>
            <div class="stat-box"><span class="stat-box-val c-purple" id="s-frm">0</span><span class="stat-box-lbl">Freemium</span></div>
            <div class="stat-box"><span class="stat-box-val c-blue" id="s-paid">0</span><span class="stat-box-lbl">Tarif public</span></div>
            <div class="stat-box"><span class="stat-box-val c-amber" id="s-devis">0</span><span class="stat-box-lbl">Sur devis</span></div>
            <div class="stat-box"><span class="stat-box-val c-accent" id="s-total">0</span><span class="stat-box-lbl">Total PAs</span></div>
        </div>

        <!-- CONTROLS -->
        <div class="tarifs-controls">
            <div class="tarifs-search-wrap">
                <span class="tarifs-search-icon">🔍</span>
                <input id="tarifs-search" type="text" class="tarifs-search-inp" placeholder="Rechercher par nom, offre, cible…">
            </div>
            <div class="tarifs-chips">
                <button class="tarifs-chip on"  data-f="all">Tous</button>
                <button class="tarifs-chip"     data-f="free">✅ Gratuit</button>
                <button class="tarifs-chip"     data-f="freemium">✨ Freemium</button>
                <button class="tarifs-chip"     data-f="paid">💶 Tarif public</button>
                <button class="tarifs-chip"     data-f="devis">📩 Sur devis</button>
            </div>
            <select id="tarifs-sort" class="tarifs-sort-sel">
                <option value="alpha">A → Z</option>
                <option value="pa">Prix ↑</option>
                <option value="pd">Prix ↓</option>
            </select>
            <span class="tarifs-count" id="tarifs-count">47 plateformes</span>
        </div>

        <!-- CALENDRIER -->
        <div class="tarifs-section-hdr">📅 Calendrier d'obligation</div>
        <div class="tarifs-cal-row">
            <div class="tarifs-cal-card">
                <div class="tarifs-cal-date">Septembre 2026</div>
                <div class="tarifs-cal-lbl">📥 <strong>Réception obligatoire</strong><br>pour toutes les entreprises</div>
            </div>
            <div class="tarifs-cal-card">
                <div class="tarifs-cal-date">Septembre 2026</div>
                <div class="tarifs-cal-lbl">📤 <strong>Émission obligatoire</strong><br>pour GE & ETI</div>
            </div>
            <div class="tarifs-cal-card">
                <div class="tarifs-cal-date">Septembre 2027</div>
                <div class="tarifs-cal-lbl">📤 <strong>Émission obligatoire</strong><br>pour TPE, PME & AE</div>
            </div>
        </div>

        <!-- SYNTHESE -->
        <div class="tarifs-section-hdr">📊 Synthèse tarifaire</div>
        <div class="tarifs-synth-row" id="tarifs-synth-row"></div>

        <!-- GRID -->
        <div class="tarifs-section-hdr">🏢 Toutes les plateformes</div>
        <div class="tarifs-grid" id="tarifs-grid"></div>
    </div>

    <!-- FLOATING COMPARE BAR -->
    <div class="compare-bar" id="compare-bar">
        <div class="compare-info" id="compare-bar-info">Sélectionnez au moins 2 plateformes pour comparer</div>
        <div class="compare-actions">
            <button class="btn btn-secondary btn-compare-action" onclick="clearComparison()">Réinitialiser</button>
            <button class="btn btn-primary btn-compare-action" id="btn-trigger-compare" onclick="openComparisonModal()">Comparer les plateformes</button>
        </div>
    </div>

    <!-- COMPARISON MODAL -->
    <div class="modal" id="comparison-modal">
        <div class="modal-container">
            <div class="modal-header">
                <h2 class="modal-title">Tableau de Comparaison Multicritères</h2>
                <button class="modal-close" onclick="closeComparisonModal()">&times;</button>
            </div>
            <div class="modal-content">
                <div class="comparison-table-wrapper" id="comparison-matrix-container">
                    <!-- Dynamic Matrix Table -->
                </div>
            </div>
        </div>
    </div>

    <!-- DETAILS MODAL -->
    <div class="modal" id="details-modal">
        <div class="modal-container" style="max-width: 1000px;">
            <div class="modal-header">
                <h2 class="modal-title" id="details-modal-title">Détails de la Plateforme</h2>
                <button class="modal-close" onclick="closeDetailsModal()">&times;</button>
            </div>
            <div class="modal-content" id="details-modal-content">
                <!-- Dynamic detailed view -->
            </div>
        </div>
    </div>

    <!-- INJECT JSON DATA -->
    <script>
        const PAS_DATA = """ + json.dumps(pa_data, ensure_ascii=False) + """;
        const PAS_TARIFS_DATA = """ + json.dumps(prix_data, ensure_ascii=False) + """;
        const selectedCompareIds = new Set();

        const CRITERIA_GROUPS = [
            {
                name: "Général",
                fields: [
                    { key: "cible_visee", label: "Cible visée", type: "text", parent: "general" },
                    { key: "utilisation_cabinet_et_dossiers_clients", label: "Usage Cabinet Experts", type: "bool", parent: "general" },
                    { key: "fait_partie_d_une_suite_logicielle", label: "Intégration Suite Logicielle", type: "suite", parent: "general" }
                ]
            },
            {
                name: "Facturation & Paiement",
                fields: [
                    { key: "creation_ou_transformation_facture_facturx", label: "Création Factur-X", type: "bool", parent: "facturation_et_paiement" },
                    { key: "creation_ou_transformation_facture_cii", label: "Création CII", type: "bool", parent: "facturation_et_paiement" },
                    { key: "creation_ou_transformation_facture_ubl", label: "Création UBL", type: "bool", parent: "facturation_et_paiement" },
                    { key: "emission_et_reception_factures_hors_perimetre_e_invoicing", label: "Factures hors périmètre", type: "bool", parent: "facturation_et_paiement" },
                    { key: "emission_et_reception_formats_autres_que_socle_minimal", label: "Formats hors socle", type: "text_or_bool", parent: "facturation_et_paiement" },
                    { key: "module_de_saisie_en_ligne_des_factures", label: "Saisie en ligne des factures", type: "bool", parent: "facturation_et_paiement" },
                    { key: "gestion_des_workflows_de_validation_des_factures", label: "Workflow validation factures", type: "bool", parent: "facturation_et_paiement" },
                    { key: "gestion_des_workflows_de_validation_des_paiements", label: "Workflow validation paiements", type: "bool", parent: "facturation_et_paiement" },
                    { key: "nombre_de_statuts_cycle_de_vie_geres_hors_obligatoires", label: "Statuts gérés optionnels", type: "text", parent: "facturation_et_paiement" },
                    { key: "service_de_paiement_disponible", label: "Service de paiement disponible", type: "text", parent: "facturation_et_paiement" }
                ]
            },
            {
                name: "Services Complémentaires",
                fields: [
                    { key: "module_ocr_integre", label: "Module OCR intégré", type: "bool", parent: "services_complementaires" },
                    { key: "rapprochement_automatique_factures_et_paiements", label: "Rapprochement factures & paiements", type: "bool", parent: "services_complementaires" },
                    { key: "gestion_des_relances_factures_clients", label: "Relances factures clients", type: "bool", parent: "services_complementaires" },
                    { key: "possibilite_de_saisie_manuelle_des_z_de_caisse", label: "Saisie manuelle Z caisse", type: "bool", parent: "services_complementaires" },
                    { key: "generation_d_un_e_reporting_norme", label: "Génération e-Reporting normé", type: "bool", parent: "services_complementaires" },
                    { key: "nombre_de_cas_d_usage_geres_sur_42", label: "Nombre cas d'usage gérés", type: "text", parent: "services_complementaires" },
                    { key: "module_de_controle_de_validite_des_informations", label: "Contrôle de validité des infos", type: "bool", parent: "services_complementaires" },
                    { key: "module_complet_de_gestion_commerciale", label: "Module gestion commerciale", type: "bool", parent: "services_complementaires" },
                    { key: "module_de_financement_des_factures_integre", label: "Module financement factures", type: "bool", parent: "services_complementaires" },
                    { key: "service_d_archivage_des_factures_integre", label: "Service d'archivage intégré", type: "bool", parent: "services_complementaires" },
                    { key: "signature_scellement_des_factures_electroniques", label: "Signature / Scellement électronique", type: "text_or_bool", parent: "services_complementaires" },
                    { key: "generation_de_tableau_de_bord_de_suivi", label: "Génération tableaux de bord", type: "bool", parent: "services_complementaires" }
                ]
            },
            {
                name: "Interopérabilité",
                fields: [
                    { key: "nombre_de_pa_interfacees", label: "PA interfacées", type: "text", parent: "interoperabilite" },
                    { key: "point_d_acces_peppol", label: "Point d'accès PEPPOL", type: "bool", parent: "interoperabilite" },
                    { key: "api_disponibles", label: "APIs disponibles", type: "text", parent: "interoperabilite" },
                    { key: "recuperation_simple_de_ses_donnees_changement_pa", label: "Récupération facile données", type: "bool", parent: "interoperabilite" },
                    { key: "integration_comptable", label: "Intégration outils comptables", type: "text", parent: "interoperabilite" }
                ]
            },
            {
                name: "Certification & Accès",
                fields: [
                    { key: "perimetre_de_certification_iso_27001", label: "Périmètre ISO 27001", type: "text", parent: "certification" },
                    { key: "inscription_sur_la_liste_des_immatriculations_pa_dgfip", label: "Immatriculation PA DGFIP", type: "bool", parent: "certification" },
                    { key: "acces_cloud", label: "Accès Cloud / SaaS", type: "bool", parent: "accessibilite" },
                    { key: "application_mobile_disponible", label: "Application mobile", type: "text", parent: "accessibilite" }
                ]
            },
            {
                name: "Sécurité & RGPD",
                fields: [
                    { key: "plan_de_recuperation_en_cas_de_cyberattaque", label: "Plan cyberattaque (PRA/PCA)", type: "text", parent: "securite_des_donnees" },
                    { key: "parametrage_des_droits_utilisateurs", label: "Droits utilisateurs fins", type: "bool", parent: "securite_des_donnees" },
                    { key: "garantie_de_confidentialite_des_donnees", label: "Garantie confidentialité", type: "text", parent: "securite_des_donnees" }
                ]
            },
            {
                name: "Support & Formation",
                fields: [
                    { key: "hotline", label: "Hotline client", type: "text", parent: "support_formation" },
                    { key: "chat_bot", label: "Chatbot support", type: "bool", parent: "support_formation" },
                    { key: "support_situe_en_france", label: "Support situé en France", type: "bool", parent: "support_formation" },
                    { key: "formation_des_utilisateurs_proposee", label: "Formation utilisateurs", type: "bool", parent: "support_formation" }
                ]
            },
            {
                name: "Structure Tarifaire",
                fields: [
                    { key: "mode_de_tarification", label: "Mode de tarification", type: "text", parent: "structure_tarifaire" },
                    { key: "cout_de_maintenance_inclus", label: "Maintenance incluse", type: "bool", parent: "structure_tarifaire" },
                    { key: "hotline_incluse", label: "Hotline incluse", type: "bool", parent: "structure_tarifaire" },
                    { key: "mises_a_jour_gratuites", label: "Mises à jour gratuites", type: "bool", parent: "structure_tarifaire" }
                ]
            }
        ];

        // Format helper functions
        function esc(s) {
            return String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        }

        function renderBool(val) {
            if (val === true || val === "true") return '<span class="val-yes">✅ Oui</span>';
            if (val === false || val === "false") return '<span class="val-no">❌ Non</span>';
            if (!val) return '<span class="val-no">❌ Non</span>';
            return val;
        }

        function renderText(val) {
            if (val === true || val === "true") return '<span class="val-yes">✅ Oui</span>';
            if (val === false || val === "false") return '<span class="val-no">❌ Non</span>';
            if (!val) return '<span style="color:var(--text-dim)">—</span>';
            return val;
        }

        // Render card grid on startup
        function renderGrid(data) {
            const grid = document.getElementById("pas-grid");
            grid.innerHTML = "";

            if (data.length === 0) {
                grid.innerHTML = '<div class="empty-state">Aucune plateforme ne correspond aux critères sélectionnés.</div>';
                return;
            }

            data.forEach(pa => {
                const card = document.createElement("div");
                card.className = "pa-card";

                const isChecked = selectedCompareIds.has(pa.name) ? "checked" : "";
                
                const target = pa.general?.cible_visee || "TPE/PME";
                const isCabinet = pa.general?.utilisation_cabinet_et_dossiers_clients;
                
                // Key features as small flex list of badges inside the card
                const ocr_val = pa.services_complementaires?.module_ocr_integre;
                const peppol_val = pa.interoperabilite?.point_d_access_peppol || pa.interoperabilite?.point_d_acces_peppol;
                const arch_val = pa.services_complementaires?.service_d_archivage_des_factures_integre;
                const api_val = pa.interoperabilite?.api_disponibles;

                card.innerHTML = `
                    <div class="pa-card-header">
                        <h2 class="pa-name" title="${pa.name}">${pa.name}</h2>
                        <div class="select-compare-container">
                            <label class="select-compare-label">
                                <input type="checkbox" class="select-compare-checkbox" value="${pa.name}" ${isChecked} onchange="toggleComparison('${pa.name}', this)">
                                Comparer
                            </label>
                        </div>
                    </div>
                    <p class="pa-desc">${pa.description || pa.presentation || ''}</p>
                    
                    <div class="pa-tags">
                        <span class="pa-tag ${isCabinet ? 'pa-tag-cabinet' : 'pa-tag-independent'}">${isCabinet ? 'Cabinet Experts' : 'Indépendant'}</span>
                        <span class="pa-tag pa-tag-cible">${target}</span>
                    </div>

                    <div class="pa-meta-summary">
                        <div class="pa-meta-tarif-row">
                            <span class="pa-meta-lbl">Tarif</span>
                            <span class="pa-meta-val-long" title="${pa.structure_tarifaire?.mode_de_tarification || 'Non spécifié'}">
                                ${pa.structure_tarifaire?.mode_de_tarification || 'Non spécifié'}
                            </span>
                        </div>
                        <div class="pa-meta-lbl" style="margin-top: 4px;">Services clés</div>
                        <div class="pa-badges-grid">
                            <div class="pa-badge-item ${ocr_val ? 'pa-badge-yes' : 'pa-badge-no'}">
                                <span>${ocr_val ? '✅' : '❌'}</span>
                                <span>OCR</span>
                            </div>
                            <div class="pa-badge-item ${peppol_val ? 'pa-badge-yes' : 'pa-badge-no'}">
                                <span>${peppol_val ? '✅' : '❌'}</span>
                                <span>PEPPOL</span>
                            </div>
                            <div class="pa-badge-item ${arch_val ? 'pa-badge-yes' : 'pa-badge-no'}">
                                <span>${arch_val ? '✅' : '❌'}</span>
                                <span>Archivage</span>
                            </div>
                            <div class="pa-badge-item ${api_val ? 'pa-badge-yes' : 'pa-badge-no'}">
                                <span>${api_val ? '✅' : '❌'}</span>
                                <span>API</span>
                            </div>
                        </div>
                    </div>

                    <div class="pa-actions">
                        <button class="btn btn-primary" onclick="showDetails('${pa.name}')">Fiche Détails</button>
                    </div>
                `;
                grid.appendChild(card);
            });

            // Update stats
            document.getElementById("count-total").innerText = data.length;
            document.getElementById("count-cabinet").innerText = data.filter(x => x.general?.utilisation_cabinet_et_dossiers_clients).length;
            document.getElementById("count-peppol").innerText = data.filter(x => x.interoperabilite?.point_d_acces_peppol).length;
        }

        // Search & Filter Trigger logic
        function filterData() {
            const searchQuery = document.getElementById("search-bar").value.toLowerCase();
            
            // Targets
            const targetFilterNodes = document.querySelectorAll(".target-filter:checked");
            const targetFilters = Array.from(targetFilterNodes).map(x => x.value);

            // Cabinet & Suite
            const filterCabinet = document.getElementById("filter-cabinet").checked;
            const filterSuite = document.getElementById("filter-suite").checked;
            const filterImmatriculation = document.getElementById("filter-immatriculation").checked;

            // Payments
            const paymentFilterNodes = document.querySelectorAll(".payment-filter:checked");
            const paymentFilters = Array.from(paymentFilterNodes).map(x => x.value);

            // Pricing
            const pricingFilterNodes = document.querySelectorAll(".pricing-filter:checked");
            const pricingFilters = Array.from(pricingFilterNodes).map(x => x.value);
            const filterMaintenance = document.getElementById("filter-maintenance").checked;
            const filterMajGratuite = document.getElementById("filter-maj-gratuite").checked;

            // Formats
            const filterFacturx = document.getElementById("filter-facturx").checked;
            const filterCii = document.getElementById("filter-cii").checked;
            const filterUbl = document.getElementById("filter-ubl").checked;
            const filterSaisie = document.getElementById("filter-saisie").checked;
            const filterWfFacture = document.getElementById("filter-wf-facture").checked;
            const filterWfPaiement = document.getElementById("filter-wf-paiement").checked;
            const filterEreporting = document.getElementById("filter-ereporting").checked;

            // Networks
            const filterPeppol = document.getElementById("filter-peppol").checked;
            const filterApi = document.getElementById("filter-api").checked;
            const filterReversibilite = document.getElementById("filter-reversibilite").checked;

            // Services
            const filterOcr = document.getElementById("filter-ocr").checked;
            const filterArchivage = document.getElementById("filter-archivage").checked;
            const filterRapprochement = document.getElementById("filter-rapprochement").checked;
            const filterRelances = document.getElementById("filter-relances").checked;
            const filterSignature = document.getElementById("filter-signature").checked;
            const filterTableau = document.getElementById("filter-tableau").checked;
            const filterControleValidite = document.getElementById("filter-controle-validite").checked;
            const filterGescom = document.getElementById("filter-gescom").checked;
            const filterFinancement = document.getElementById("filter-financement").checked;

            // Sec & Support
            const filterIso = document.getElementById("filter-iso").checked;
            const filterCloud = document.getElementById("filter-cloud").checked;
            const filterMobile = document.getElementById("filter-mobile").checked;
            const filterFrance = document.getElementById("filter-france").checked;
            const filtered = PAS_DATA.filter(pa => {
                // Search query matching name / description / presentation
                const nameMatch = pa.name.toLowerCase().includes(searchQuery);
                const descMatch = (pa.description || "").toLowerCase().includes(searchQuery);
                const presMatch = (pa.presentation || "").toLowerCase().includes(searchQuery);
                if (searchQuery && !nameMatch && !descMatch && !presMatch) return false;

                // Target match
                if (targetFilters.length > 0) {
                    const target = (pa.general?.cible_visee || "").toUpperCase();
                    const targetMatches = targetFilters.some(tf => target.includes(tf.toUpperCase()));
                    if (!targetMatches) return false;
                }

                // Cabinet & Suite
                if (filterCabinet && !pa.general?.utilisation_cabinet_et_dossiers_clients) return false;
                if (filterSuite && (!pa.general?.fait_partie_d_une_suite_logicielle || pa.general?.fait_partie_d_une_suite_logicielle === false)) return false;
                if (filterImmatriculation && !pa.certification?.inscription_sur_la_liste_des_immatriculations_pa_dgfip) return false;

                // Payments Filter
                if (paymentFilters.length > 0) {
                    const paymentVal = (pa.facturation_et_paiement?.service_de_paiement_disponible || "").toLowerCase();
                    const paymentMatches = paymentFilters.some(pf => {
                        if (pf === "aucun") {
                            return paymentVal.includes("aucun") || paymentVal === "";
                        }
                        return paymentVal.includes(pf);
                    });
                    if (!paymentMatches) return false;
                }

                // Pricing Filter
                if (pricingFilters.length > 0) {
                    const pricingVal = (pa.structure_tarifaire?.mode_de_tarification || "").toLowerCase();
                    const pricingMatches = pricingFilters.some(pf => {
                        if (pf === "gratuit") {
                            return pricingVal.includes("gratuit") || pricingVal.includes("inclus");
                        }
                        if (pf === "abonnement") {
                            return pricingVal.includes("abonnement") || pricingVal.includes("forfait") || pricingVal.includes("prix compris");
                        }
                        if (pf === "volume") {
                            return pricingVal.includes("volume") || pricingVal.includes("usage") || pricingVal.includes("facture émission") || pricingVal.includes("consommation");
                        }
                        return false;
                    });
                    if (!pricingMatches) return false;
                }

                if (filterMaintenance && (!pa.structure_tarifaire?.cout_de_maintenance_inclus || !pa.structure_tarifaire?.hotline_incluse)) return false;
                if (filterMajGratuite && !pa.structure_tarifaire?.mises_a_jour_gratuites) return false;

                // Formats
                if (filterFacturx && !pa.facturation_et_paiement?.creation_ou_transformation_facture_facturx) return false;
                if (filterCii && !pa.facturation_et_paiement?.creation_ou_transformation_facture_cii) return false;
                if (filterUbl && !pa.facturation_et_paiement?.creation_ou_transformation_facture_ubl) return false;
                if (filterSaisie && !pa.facturation_et_paiement?.module_de_saisie_en_ligne_des_factures) return false;
                if (filterWfFacture && !pa.facturation_et_paiement?.gestion_des_workflows_de_validation_des_factures) return false;
                if (filterWfPaiement && !pa.facturation_et_paiement?.gestion_des_workflows_de_validation_des_paiements) return false;
                if (filterEreporting && !pa.services_complementaires?.generation_d_un_e_reporting_norme) return false;

                // Networks
                if (filterPeppol && !pa.interoperabilite?.point_d_acces_peppol) return false;
                if (filterApi && (!pa.interoperabilite?.api_disponibles || pa.interoperabilite?.api_disponibles === false || pa.interoperabilite?.api_disponibles === "")) return false;
                if (filterReversibilite && !pa.interoperabilite?.recuperation_simple_de_ses_donnees_changement_pa) return false;

                // Services
                if (filterOcr && !pa.services_complementaires?.module_ocr_integre) return false;
                if (filterArchivage && !pa.services_complementaires?.service_d_archivage_des_factures_integre) return false;
                if (filterRapprochement && !pa.services_complementaires?.rapprochement_automatique_factures_et_paiements) return false;
                if (filterRelances && !pa.services_complementaires?.gestion_des_relances_factures_clients) return false;
                if (filterSignature && (!pa.services_complementaires?.signature_scellement_des_factures_electroniques || pa.services_complementaires?.signature_scellement_des_factures_electroniques === false)) return false;
                if (filterTableau && !pa.services_complementaires?.generation_de_tableau_de_bord_de_suivi) return false;
                if (filterControleValidite && !pa.services_complementaires?.module_de_controle_de_validite_des_informations) return false;
                if (filterGescom && !pa.services_complementaires?.module_complet_de_gestion_commerciale) return false;
                if (filterFinancement && !pa.services_complementaires?.module_de_financement_des_factures_integre) return false;

                // Sec & Support
                if (filterIso && (!pa.certification?.perimetre_de_certification_iso_27001 || pa.certification?.perimetre_de_certification_iso_27001 === false || pa.certification?.perimetre_de_certification_iso_27001 === "")) return false;
                if (filterCloud && !pa.accessibilite?.acces_cloud) return false;
                if (filterMobile && (!pa.accessibilite?.application_mobile_disponible || pa.accessibilite?.application_mobile_disponible === "Aucune")) return false;
                if (filterFrance && !pa.support_formation?.support_situe_en_france) return false;

                return true;
            });

            renderGrid(filtered);
        }

        // Compare bar controller
        function toggleComparison(paName, checkboxElement) {
            if (checkboxElement.checked) {
                if (selectedCompareIds.size >= 4) {
                    alert("Vous pouvez comparer au maximum 4 plateformes à la fois.");
                    checkboxElement.checked = false;
                    return;
                }
                selectedCompareIds.add(paName);
            } else {
                selectedCompareIds.delete(paName);
            }

            updateCompareBar();
        }

        function updateCompareBar() {
            const bar = document.getElementById("compare-bar");
            const info = document.getElementById("compare-bar-info");
            
            if (selectedCompareIds.size > 0) {
                bar.classList.add("show");
                if (selectedCompareIds.size >= 2) {
                    info.innerHTML = `<strong>${selectedCompareIds.size}</strong> plateforme(s) sélectionnée(s) pour comparaison`;
                    document.getElementById("btn-trigger-compare").removeAttribute("disabled");
                } else {
                    info.innerHTML = `Sélectionnez encore au moins 1 plateforme à comparer`;
                    document.getElementById("btn-trigger-compare").setAttribute("disabled", "true");
                }
            } else {
                bar.classList.remove("show");
            }
        }

        function clearComparison() {
            selectedCompareIds.clear();
            document.querySelectorAll(".select-compare-checkbox").forEach(cb => cb.checked = false);
            updateCompareBar();
        }

        // Open/Close Modals
        function openComparisonModal() {
            const modal = document.getElementById("comparison-modal");
            const container = document.getElementById("comparison-matrix-container");
            
            // Build the comparison matrix dynamically
            const pasToCompare = PAS_DATA.filter(pa => selectedCompareIds.has(pa.name));
            
            let matrixHtml = `<table class="comparison-table"><thead><tr><th>Critère / Fonctionnalité</th>`;
            pasToCompare.forEach(pa => {
                matrixHtml += `<th>${pa.name}</th>`;
            });
            matrixHtml += `</tr></thead><tbody>`;

            CRITERIA_GROUPS.forEach(group => {
                matrixHtml += `<tr class="row-category"><td colspan="${pasToCompare.length + 1}">${group.name}</td></tr>`;
                
                group.fields.forEach(field => {
                    matrixHtml += `<tr><td class="row-feature-title">${field.label}</td>`;
                    pasToCompare.forEach(pa => {
                        const val = pa[field.parent]?.[field.key];
                        const displayVal = (field.type === "bool") ? renderBool(val) : renderText(val);
                        matrixHtml += `<td>${displayVal}</td>`;
                    });
                    matrixHtml += `</tr>`;
                });
            });

            // Atouts row
            matrixHtml += `<tr class="row-category"><td colspan="${pasToCompare.length + 1}">Synthèse & Atouts</td></tr>`;
            matrixHtml += `<tr><td class="row-feature-title">Atouts principaux</td>`;
            pasToCompare.forEach(pa => {
                const atouts = pa.autres?.les_3_atouts_de_la_solution || "";
                const listItems = atouts.split('|').map(x => `<li>${x.trim()}</li>`).join('');
                matrixHtml += `<td><ul style="padding-left:16px; font-size:0.85rem; color:var(--text-secondary);">${listItems}</ul></td>`;
            });
            matrixHtml += `</tr>`;

            matrixHtml += `</tbody></table>`;
            container.innerHTML = matrixHtml;

            modal.style.display = "flex";
            setTimeout(() => modal.classList.add("show"), 10);
        }

        function closeComparisonModal() {
            const modal = document.getElementById("comparison-modal");
            modal.classList.remove("show");
            setTimeout(() => modal.style.display = "none", 300);
        }

        function showDetails(paName) {
            const modal = document.getElementById("details-modal");
            const pa = PAS_DATA.find(x => x.name === paName);
            
            document.getElementById("details-modal-title").innerText = pa.name;
            
            const detailContent = document.getElementById("details-modal-content");
            
            // Generate detailed layout
            let sectionsHtml = "";
            CRITERIA_GROUPS.forEach(group => {
                let fieldsHtml = "";
                group.fields.forEach(field => {
                    const val = pa[field.parent]?.[field.key];
                    const displayVal = (field.type === "bool") ? renderBool(val) : renderText(val);
                    fieldsHtml += `
                        <div class="detail-field-item">
                            <span class="detail-field-name">${field.label}</span>
                            <span class="detail-field-value">${displayVal}</span>
                        </div>
                    `;
                });

                sectionsHtml += `
                    <div class="detail-card-box">
                        <h3>${group.name}</h3>
                        <div class="detail-field-list">
                            ${fieldsHtml}
                        </div>
                    </div>
                `;
            });

            const atouts = pa.autres?.les_3_atouts_de_la_solution || "";
            const atoutsHtml = atouts.split('|').map(x => `<div class="atouts-item">🎯 ${x.trim()}</div>`).join('');

            detailContent.innerHTML = `
                <div class="detail-grid">
                    <div class="detail-main">
                        <div class="detail-card-box">
                            <h3>Présentation & Description</h3>
                            <p style="font-size:0.95rem; line-height:1.6; color:var(--text-secondary); margin-bottom:16px;">${pa.presentation || ''}</p>
                            <p style="font-size:0.9rem; line-height:1.6; color:var(--text-dim);">${pa.description || ''}</p>
                        </div>

                        <div class="detail-card-box">
                            <h3>Atouts Majeurs</h3>
                            <div class="atouts-list">
                                ${atoutsHtml || '<p style="color:var(--text-dim)">Aucun atout listé.</p>'}
                            </div>
                        </div>

                        ${pa.autres?.prerequis ? `
                        <div class="detail-card-box">
                            <h3>Prérequis Techniques</h3>
                            <p style="font-size:0.9rem; color:var(--text-secondary);">${pa.autres.prerequis}</p>
                        </div>
                        ` : ''}
                    </div>

                    <div class="detail-sidebar">
                        ${sectionsHtml}
                    </div>
                </div>
            `;

            modal.style.display = "flex";
            setTimeout(() => modal.classList.add("show"), 10);
        }

        function closeDetailsModal() {
            const modal = document.getElementById("details-modal");
            modal.classList.remove("show");
            setTimeout(() => modal.style.display = "none", 300);
        }

        // Event Listeners
        document.getElementById("search-bar").addEventListener("input", filterData);
        document.querySelectorAll(".target-filter").forEach(cb => cb.addEventListener("change", filterData));
        document.getElementById("filter-cabinet").addEventListener("change", filterData);
        document.getElementById("filter-suite").addEventListener("change", filterData);
        document.getElementById("filter-immatriculation").addEventListener("change", filterData);

        document.querySelectorAll(".payment-filter").forEach(cb => cb.addEventListener("change", filterData));
        document.querySelectorAll(".pricing-filter").forEach(cb => cb.addEventListener("change", filterData));
        document.getElementById("filter-maintenance").addEventListener("change", filterData);
        document.getElementById("filter-maj-gratuite").addEventListener("change", filterData);
        
        document.getElementById("filter-facturx").addEventListener("change", filterData);
        document.getElementById("filter-cii").addEventListener("change", filterData);
        document.getElementById("filter-ubl").addEventListener("change", filterData);
        document.getElementById("filter-saisie").addEventListener("change", filterData);
        document.getElementById("filter-wf-facture").addEventListener("change", filterData);
        document.getElementById("filter-wf-paiement").addEventListener("change", filterData);
        document.getElementById("filter-ereporting").addEventListener("change", filterData);
        
        document.getElementById("filter-peppol").addEventListener("change", filterData);
        document.getElementById("filter-api").addEventListener("change", filterData);
        document.getElementById("filter-reversibilite").addEventListener("change", filterData);

        document.getElementById("filter-ocr").addEventListener("change", filterData);
        document.getElementById("filter-archivage").addEventListener("change", filterData);
        document.getElementById("filter-rapprochement").addEventListener("change", filterData);
        document.getElementById("filter-relances").addEventListener("change", filterData);
        document.getElementById("filter-signature").addEventListener("change", filterData);
        document.getElementById("filter-tableau").addEventListener("change", filterData);
        document.getElementById("filter-controle-validite").addEventListener("change", filterData);
        document.getElementById("filter-gescom").addEventListener("change", filterData);
        document.getElementById("filter-financement").addEventListener("change", filterData);

        document.getElementById("filter-iso").addEventListener("change", filterData);
        document.getElementById("filter-cloud").addEventListener("change", filterData);
        document.getElementById("filter-mobile").addEventListener("change", filterData);
        document.getElementById("filter-france").addEventListener("change", filterData);

        // Grid layout toggler
        document.querySelectorAll(".layout-btn").forEach(btn => {
            btn.addEventListener("click", () => {
                document.querySelectorAll(".layout-btn").forEach(b => b.classList.remove("active"));
                btn.classList.add("active");
                
                const cols = btn.getAttribute("data-cols");
                const grid = document.getElementById("pas-grid");
                
                // Clear grid classes
                grid.classList.remove("cols-2", "cols-3", "cols-4");
                
                if (cols !== "auto") {
                    grid.classList.add(`cols-${cols}`);
                }
            });
        });

        // ── TARIFS VIEW LOGIC ──
        const PAS_TARIFS = PAS_TARIFS_DATA.plateformes_agrees;

        const SYNTH = {
          gratuites: ["API FIRST BY DOUGS","CHAINTRUST BY VISMA","DEXT BY IRIS","DIGIPHARMACIE","INDY (Essentiel)","IPAIDTHAT","JEFACTURE.COM ECMA","KOLECTO","MACOMPTA.FR","OPEN BEE FRANCE","PENNYLANE (Plan 0€)","SUPER PDP","TIIME (Free)"],
          prix_publics: [{nom:"Qonto",p:"9€/mois"},{nom:"Pennylane",p:"14€/mois"},{nom:"Tiime",p:"Gratuit (17,99€/mois Start)"},{nom:"Indy",p:"Gratuit (9€/mois Plus)"},{nom:"Sellsy",p:"29€/mois"},{nom:"Axonaut",p:"34,99€/mois"}],
          fourchette: {min:"9€/mois (Qonto Basic)", max:"199€/mois (Qonto Enterprise)", moy:"15–40€/mois"},
          inclus: ["Émission & réception factures électroniques","Conformité Factur-X, UBL 2.1, CII","Transmission au PPF et DGFiP","Archivage légal (10 ans min.)","Tableau de bord de suivi"]
        };

        function getTarifType(pa) {
          const t = pa.type_tarification || '';
          const p = pa.prix || '';
          if (t === 'Freemium') return 'freemium';
          if (p === 'Gratuit' || p.startsWith('Gratuit')) return 'free';
          if (p === 'Sur devis' || t === 'Non public' || t.toLowerCase().includes('devis')) return 'devis';
          return 'paid';
        }

        const T_BADGE_MAP = { free:'t-badge-free', paid:'t-badge-paid', devis:'t-badge-devis', freemium:'t-badge-freemium' };
        const T_BADGE_LBL = { free:'Gratuit', paid:'Payant', devis:'Sur devis', freemium:'Freemium' };
        const T_PRICE_CLS = { free:'t-p-free', paid:'t-p-paid', devis:'t-p-devis', freemium:'t-p-freemium' };

        function renderTarifOffers(pa) {
          if (!pa.offres_detaillées?.length) return '';
          return `<div class="t-offers">
            <div class="t-offers-lbl">Détail des offres</div>
            ${pa.offres_detaillées.map(o => `
              <div class="t-offer-item">
                <span class="t-offer-name">${esc(o.nom)}</span>
                <span class="t-offer-price">${esc(o.prix)}${o.reduction ? ` <span class="t-offer-reduce">−${o.reduction}</span>` : ''}</span>
              </div>`).join('')}
          </div>`;
        }

        function renderTarifCard(pa) {
          const type = getTarifType(pa);
          const feats = (pa.fonctionnalités_incluses || []).slice(0, 7);
          const fmts  = pa.formats_supportés || [];
          const noteIsNoSite = pa.note === 'Site officiel non trouvé';

          return `<div class="t-card" data-type="${type}" data-p="${pa.prix_minimal_estime ?? 99999}">
            <span class="t-badge ${T_BADGE_MAP[type]}">${T_BADGE_LBL[type]}</span>
            <div class="t-card-name">${esc(pa.nom)}</div>
            ${pa.offre_nom ? `<div class="t-card-offre">${esc(pa.offre_nom)}</div>` : ''}
            <div class="t-card-price ${T_PRICE_CLS[type]}">${esc(pa.prix)}</div>
            <div class="t-card-price-type">${esc(pa.type_tarification || '')}</div>
            ${pa.cible && pa.cible !== 'Non spécifié' ? `<div class="t-card-cible">🎯 ${esc(pa.cible)}</div>` : ''}
            <div class="t-card-site">
              ${pa.site_officiel
                ? `🌐 <a href="${esc(pa.site_officiel)}" target="_blank" rel="noopener">${esc(pa.site_officiel.replace(/^https?:\\/\\//,''))}</a>`
                : `<span class="t-card-no-site">🔒 Site officiel non répertorié</span>`}
            </div>
            ${pa.contact ? `<div class="t-card-contact">✉️ ${esc(pa.contact)}</div>` : ''}
            ${renderTarifOffers(pa)}
            ${feats.length ? `
              <div class="t-feats-lbl">Ce qui est inclus</div>
              <div class="t-feats">${feats.map(f => `<div class="t-feat"><span class="t-feat-check">✔</span><span>${esc(f)}</span></div>`).join('')}</div>` : ''}
            ${fmts.length ? `<div class="t-formats">${fmts.map(f => `<span class="t-fmt">${esc(f)}</span>`).join('')}</div>` : ''}
            <div class="t-card-foot">
              <span>
                ${pa.note && !noteIsNoSite ? `<span class="t-card-note">⭐ ${esc(pa.note)}</span>` : ''}
                ${pa.essai_gratuit ? `<span class="t-card-trial">🎁 ${esc(pa.essai_gratuit)}</span>` : ''}
              </span>
            </div>
          </div>`;
        }

        function buildTarifsSynth() {
          document.getElementById('tarifs-synth-row').innerHTML = `
            <div class="tarifs-synth-card">
              <div class="tarifs-synth-title">✅ Plateformes gratuites</div>
              <div class="tarifs-synth-list">${SYNTH.gratuites.map(n => `<div class="tarifs-synth-item"><span class="tarifs-bullet tarifs-b-green"></span><span>${esc(n)}</span></div>`).join('')}</div>
            </div>
            <div class="tarifs-synth-card">
              <div class="tarifs-synth-title">💶 Tarifs publics connus</div>
              <div class="tarifs-synth-list">${SYNTH.prix_publics.map(x => `<div class="tarifs-synth-item"><span class="tarifs-bullet tarifs-b-blue"></span><span><strong>${esc(x.nom)}</strong> — ${esc(x.p)}</span></div>`).join('')}</div>
            </div>
            <div class="tarifs-synth-card">
              <div class="tarifs-synth-title">📊 Fourchette tarifaire</div>
              <div class="tarifs-synth-list">
                <div class="tarifs-synth-item"><span class="tarifs-bullet tarifs-b-amber"></span><span>Min : <strong>${SYNTH.fourchette.min}</strong></span></div>
                <div class="tarifs-synth-item"><span class="tarifs-bullet tarifs-b-amber"></span><span>Max : <strong>${SYNTH.fourchette.max}</strong></span></div>
                <div class="tarifs-synth-item"><span class="tarifs-bullet tarifs-b-amber"></span><span>Moy. TPE/PME : <strong>${SYNTH.fourchette.moy}</strong></span></div>
                <div class="tarifs-synth-item"><span class="tarifs-bullet tarifs-b-gray"></span><span>Sur devis : <strong>31 plateformes</strong></span></div>
              </div>
            </div>
            <div class="tarifs-synth-card">
              <div class="tarifs-synth-title">📦 Inclus de base (toutes PAs)</div>
              <div class="tarifs-synth-list">${SYNTH.inclus.map(i => `<div class="tarifs-synth-item"><span class="tarifs-bullet tarifs-b-green"></span><span>${esc(i)}</span></div>`).join('')}</div>
            </div>
          `;
        }

        let activeTarifFilter = 'all';

        function updateTarifsStats(list) {
          document.getElementById('s-free').textContent  = list.filter(p => getTarifType(p)==='free').length;
          document.getElementById('s-frm').textContent   = list.filter(p => getTarifType(p)==='freemium').length;
          document.getElementById('s-paid').textContent  = list.filter(p => getTarifType(p)==='paid').length;
          document.getElementById('s-devis').textContent = list.filter(p => getTarifType(p)==='devis').length;
          document.getElementById('s-total').textContent = list.length;
        }

        function renderTarifs() {
          const q    = document.getElementById('tarifs-search').value.toLowerCase().trim();
          const sort = document.getElementById('tarifs-sort').value;
          let list   = [...PAS_TARIFS];

          if (activeTarifFilter !== 'all') list = list.filter(p => getTarifType(p) === activeTarifFilter);
          if (q) list = list.filter(p =>
            p.nom.toLowerCase().includes(q) ||
            (p.offre_nom||'').toLowerCase().includes(q) ||
            (p.cible||'').toLowerCase().includes(q) ||
            (p.type_tarification||'').toLowerCase().includes(q) ||
            (p.fonctionnalités_incluses||[]).some(f => f.toLowerCase().includes(q))
          );

          if (sort === 'alpha') list.sort((a,b) => a.nom.localeCompare(b.nom, 'fr'));
          else if (sort === 'pa')   list.sort((a,b) => (a.prix_minimal_estime??99999)-(b.prix_minimal_estime??99999));
          else if (sort === 'pd')   list.sort((a,b) => (b.prix_minimal_estime??-1)-(a.prix_minimal_estime??-1));

          updateTarifsStats(list);
          document.getElementById('tarifs-count').textContent = `${list.length} plateforme${list.length!==1?'s':''}`;
          document.getElementById('tarifs-grid').innerHTML = list.length
            ? list.map(renderTarifCard).join('')
            : `<div class="empty"><div class="empty-icon">🔍</div>Aucun résultat pour cette recherche.</div>`;
        }

        // ── PAGE SWAP LOGIC ──
        function showPage(pageId) {
            document.querySelectorAll('.app-page').forEach(p => p.style.display = 'none');
            document.getElementById('page-' + pageId).style.display = 'block';
            
            // Update active tab in nav
            document.querySelectorAll('.top-nav-tab').forEach(tab => {
                if (tab.getAttribute('data-page') === pageId) {
                    tab.classList.add('active');
                } else {
                    tab.classList.remove('active');
                }
            });

            // If switching to tarifs, trigger render/build once
            if (pageId === 'tarifs') {
                buildTarifsSynth();
                renderTarifs();
            }
        }

        // Initial render & setups
        window.addEventListener("DOMContentLoaded", () => {
            renderGrid(PAS_DATA);

            // Set up Tarifs listeners
            document.getElementById('tarifs-search').addEventListener('input', renderTarifs);
            document.getElementById('tarifs-sort').addEventListener('change', renderTarifs);
            document.querySelectorAll('.tarifs-chip').forEach(btn => {
                btn.addEventListener('click', () => {
                    document.querySelectorAll('.tarifs-chip').forEach(b => b.classList.remove('on'));
                    btn.classList.add('on');
                    activeTarifFilter = btn.dataset.f;
                    renderTarifs();
                });
            });
        });
    </script>
</body>
</html>
"""

    with open(os.path.join(current_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_template)

    print(f"HTML generated successfully with {len(pa_data)} entries.")

    # Synchroniser prix.html avec le dernier prix.json
    prix_html_path = os.path.join(current_dir, 'prix.html')
    if os.path.exists(prix_html_path):
        try:
            with open(prix_html_path, 'r', encoding='utf-8') as f:
                prix_html_content = f.read()
            
            import re
            # Remplace la variable hardcodée const PAS = [...]; par les données fraîches de prix.json
            pattern = r'const PAS\s*=\s*\[.*\]\s*;'
            replacement = f'const PAS = {json.dumps(prix_data["plateformes_agrees"], ensure_ascii=False)};'
            
            new_prix_html = re.sub(pattern, replacement, prix_html_content)
            
            with open(prix_html_path, 'w', encoding='utf-8') as f:
                f.write(new_prix_html)
            print("prix.html mis à jour avec succès depuis prix.json.")
        except Exception as e:
            print(f"Erreur lors de la mise à jour de prix.html : {e}")

if __name__ == '__main__':
    build_html()
